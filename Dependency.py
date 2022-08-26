import os
import re
import shutil
import wget

from zipfile import ZipFile

from colors import param
from log import log_error, log_info, log_verbose
from Dirs import Dirs

class Dependency:
    def __init__(self, name: str, is_verbose: bool, dirs: Dirs):
        self.__name = name
        self.__is_verbose = is_verbose
        self.__dirs = dirs

    def name(self):
        return self.__name
    
    def is_verbose(self):
        return self.__is_verbose

    def download(self):
        pass

    def build(self):
        pass

    def install(self):
        pass

    def setup_cmake(self):
        pass

    # def copy_include_from_cache(self, cache_src: str, include_dest):
    #     self.__dirs.copy_include_from_cache(self.__name, self.__is_verbose, f"{self.__name}/{cache_src}", f"{self.__name}/{include_dest}")

    # def log_info(self, message):
    #     print(f"[{magenta(self.__name)}] [{LOG_INFO}] {message}")

    # def log_verbose(self, message):
    #     if self.is_verbose:
    #         print(f"[{magenta(self.__name)}] [{LOG_VERBOSE}] {message}")
    
    # def log_error(self, message):
    #     print(f"[{magenta(self.__name)}] [{LOG_ERROR}] {message}")
    
    def download_file(self, url: str, dest_path: str):
        if os.path.exists(dest_path):
            log_verbose(self.__name, self.__is_verbose, "File already exists: ", dest_path)
            return

        log_info(self.__name, f"Download {param(url)} -> {param(dest_path)}")
        wget.download(url, dest_path)
        print()
    
    def cache_file(self, name: str):
        return self.__dirs.cache_file(self.__name, name)
    
    def include_file(self, name: str):
        return self.__dirs.include_file(self.__name, name)

    def include_dir(self):
        return self.__dirs.include_dir(self.__name)
    
    def cmake_file(self):
        return self.__dirs.cmake_file(self.__name)
    
    def static_lib_file(self, name: str):
        return self.__dirs.static_lib_file(self.__name, name)
    
    # def make_folder(self, path):
    #     if os.path.exists(path):
    #         # self.log_verbose(f"Directory {param(path)} already exists.")
    #         return

    #     # self.log_info(f"Create directory: {param(path)}")
    #     os.mkdir(path)
            
    def copy_file(self, src: str, dest: str):
        if not os.path.exists(src):
            log_error(self.__name, "File not found: ", src)
            exit(1)
        
        if os.path.exists(dest):
            log_verbose(self.__name, self.__is_verbose, "File already exists: ", dest)
            return

        log_info(self.__name, f"Copy {param(src)} -> {param(dest)}")
        shutil.copyfile(src, dest)
    
    # def extract_zip(self, src, base_dir, test_dir):
    #     if os.path.exists(test_dir):
    #         # self.log_verbose(f"Directory {param(test_dir)} already exists.")
    #         return
        
    #     if not os.path.exists(src):
    #         # self.log_error(f"File {param(src)} does not exist.")
    #         exit(1)
        
    #     # self.log_info(f"Extract {param(src)} -> {param(base_dir)}")
    #     with zipfile.ZipFile(src, 'r') as zip:
    #         zip.extractall(base_dir)
    
    def unzip_includes(self, zip_file: ZipFile, pattern: str):
        for file_name in zip_file.namelist():
            match = re.match(pattern, file_name)
            if match:
                out_file_name = self.include_file(match.group(1))
                if os.path.exists(out_file_name):
                    log_verbose(self.__name, self.__is_verbose, "File already exists: ", out_file_name)
                    continue
                data = zip_file.read(file_name)
                with open(out_file_name, "wb") as file:
                    log_info(self.__name, f"Extract {param(file_name)} -> {param(out_file_name)}")
                    file.write(data)
    
    def unzip_static_lib(self, zip_file: ZipFile, zip_path: str, name: str):
        lib_file = self.static_lib_file(name)
        if os.path.exists(lib_file):
            return
        data = zip_file.read(zip_path)
        with open(lib_file, "wb") as file:
            log_info(self.__name, f"Extract {param(zip_path)} -> {param(lib_file)}")
            file.write(data)
    
    def __unzip_dynamic_lib_debug(self, zip_file: ZipFile, zip_path: str, name: str):
        lib_file = self.__dirs.dynamic_lib_file_debug(self.__name, name)
        if os.path.exists(lib_file):
            return
        data = zip_file.read(zip_path)
        with open(lib_file, "wb") as file:
            log_info(self.__name, f"Extract {param(zip_path)} -> {param(lib_file)}")
            file.write(data)
    
    def __unzip_dynamic_lib_release(self, zip_file: ZipFile, zip_path: str, name: str):
        lib_file = self.__dirs.dynamic_lib_file_release(self.__name, name)
        if os.path.exists(lib_file):
            return
        data = zip_file.read(zip_path)
        with open(lib_file, "wb") as file:
            log_info(self.__name, f"Extract {param(zip_path)} -> {param(lib_file)}")
            file.write(data)
    
    def unzip_dynamic_lib(self, zip_file: ZipFile, zip_path: str, name: str):
        self.__unzip_dynamic_lib_debug(zip_file, zip_path, name)
        self.__unzip_dynamic_lib_release(zip_file, zip_path, name)