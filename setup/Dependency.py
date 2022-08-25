import os
import re
import shutil
import wget
import zipfile

from setup.colors import param, magenta, green, gray, red

LOG_INFO = green("Info")
LOG_VERBOSE = gray("Verbose")
LOG_ERROR = red("Error")

class Dependency:
    def __init__(self, name, is_verbose):
        self.__name = name
        self.__is_verbose = is_verbose

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

    def log_info(self, message):
        print(f"[{magenta(self.__name)}] [{LOG_INFO}] {message}")

    def log_verbose(self, message):
        if self.is_verbose:
            print(f"[{magenta(self.__name)}] [{LOG_VERBOSE}] {message}")
    
    def log_error(self, message):
        print(f"[{magenta(self.__name)}] [{LOG_ERROR}] {message}")
    
    def download_file(self, url, dest):
        if os.path.exists(dest):
            self.log_verbose(f"File {param(dest)} already exists.")
            return

        self.log_info(f"Download: {param(url)} -> {param(dest)}")
        wget.download(url, dest)
        print()
    
    def make_folder(self, path):
        if os.path.exists(path):
            self.log_verbose(f"Directory {param(path)} already exists.")
            return

        self.log_info(f"Create directory: {param(path)}")
        os.mkdir(path)
            
    def copy_file(self, src, dest):
        if not os.path.exists(src):
            self.log_error(f"File not found: {param(src)}")
            exit(1)
        
        if os.path.exists(dest):
            self.log_verbose(f"File {param(dest)} already exists.")
            return

        self.log_info(f"Copy {param(src)} -> {param(dest)}")
        shutil.copyfile(src, dest)
    
    def extract_zip(self, src, base_dir, test_dir):
        if os.path.exists(test_dir):
            self.log_verbose(f"Directory {param(test_dir)} already exists.")
            return
        
        if not os.path.exists(src):
            self.log_error(f"File {param(src)} does not exist.")
            exit(1)
        
        self.log_info(f"Extract {param(src)} -> {param(base_dir)}")
        with zipfile.ZipFile(src, 'r') as zip:
            zip.extractall(base_dir)
    
    def extract_pattern_zip(self, zip_file: zipfile.ZipFile, pattern, base_path):
        for file_name in zip_file.namelist():
            match = re.match(pattern, file_name)
            if match:
                group1 = match.group(1)
                out_file_name = f"{base_path}/{match.group(1)}"
                if os.path.exists(out_file_name):
                    self.log_verbose(f"File {param(out_file_name)} already exists.")
                    continue
                data = zip_file.read(file_name)
                with open(out_file_name, "wb") as file:
                    self.log_info(f"Extract {param(file_name)} -> {param(out_file_name)}")
                    file.write(data)