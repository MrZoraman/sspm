# Copyright (c) 2022 MrZoraman
# 
# This software is provided 'as-is', without any express or implied
# warranty. In no event will the authors be held liable for any damages
# arising from the use of this software.

# Permission is granted to anyone to use this software for any purpose,
# including commercial applications, and to alter it and redistribute it
# freely, subject to the following restrictions:

# 1. The origin of this software must not be misrepresented; you must not
#    claim that you wrote the original software. If you use this software
#    in a product, an acknowledgment in the product documentation would be
#    appreciated but is not required.
# 2. Altered source versions must be plainly marked as such, and must not be
#    misrepresented as being the original software.
# 3. This notice may not be removed or altered from any source distribution.

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
    
    def dynamic_lib_file_debug(self, name: str):
        return self.__dirs.dynamic_lib_file_debug(self.__name, name)
    
    def dynamic_lib_file_release(self, name: str):
        return self.__dirs.dynamic_lib_file_release(self.__name, name)
    
    def lib_build_dir(self):
        return self.__dirs.lib_build_dir(self.__name)
    
    def extract_cache_zip_to_build_dir(self, zip_name:str):
        with ZipFile(self.cache_file(zip_name), 'r') as zip:
            zip.extractall(self.lib_build_dir())
            
    def copy_file(self, src: str, dest: str):
        if not os.path.exists(src):
            log_error(self.__name, "File not found: ", src)
            exit(1)
        
        if os.path.exists(dest):
            log_verbose(self.__name, self.__is_verbose, "File already exists: ", dest)
            return

        log_info(self.__name, f"Copy {param(src)} -> {param(dest)}")
        shutil.copyfile(src, dest)
    
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
    
    def unzip_static_lib(self, zip_file: ZipFile, zip_path: str):
        name = os.path.basename(zip_path)
        lib_file = self.static_lib_file(name)
        if os.path.exists(lib_file):
            return
        data = zip_file.read(zip_path)
        with open(lib_file, "wb") as file:
            log_info(self.__name, f"Extract {param(zip_path)} -> {param(lib_file)}")
            file.write(data)
    
    def __unzip_dynamic_lib_debug(self, zip_file: ZipFile, zip_path: str, name: str):
        lib_file = self.dynamic_lib_file_debug(name)
        if os.path.exists(lib_file):
            return
        data = zip_file.read(zip_path)
        with open(lib_file, "wb") as file:
            log_info(self.__name, f"Extract {param(zip_path)} -> {param(lib_file)}")
            file.write(data)
    
    def __unzip_dynamic_lib_release(self, zip_file: ZipFile, zip_path: str, name: str):
        lib_file = self.dynamic_lib_file_release(name)
        if os.path.exists(lib_file):
            return
        data = zip_file.read(zip_path)
        with open(lib_file, "wb") as file:
            log_info(self.__name, f"Extract {param(zip_path)} -> {param(lib_file)}")
            file.write(data)
    
    def unzip_dynamic_lib(self, zip_file: ZipFile, zip_path: str):
        name = os.path.basename(zip_path)
        self.__unzip_dynamic_lib_debug(zip_file, zip_path, name)
        self.__unzip_dynamic_lib_release(zip_file, zip_path, name)