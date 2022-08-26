import os
import re
import shutil
import wget
import zipfile

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
    
    # def extract_pattern_zip(self, zip_file: zipfile.ZipFile, pattern, base_path):
    #     for file_name in zip_file.namelist():
    #         match = re.match(pattern, file_name)
    #         if match:
    #             out_file_name = f"{base_path}/{match.group(1)}"
    #             if os.path.exists(out_file_name):
    #                 # self.log_verbose(f"File {param(out_file_name)} already exists.")
    #                 continue
    #             data = zip_file.read(file_name)
    #             with open(out_file_name, "wb") as file:
    #                 # self.log_info(f"Extract {param(file_name)} -> {param(out_file_name)}")
    #                 file.write(data)