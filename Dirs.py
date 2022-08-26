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
import shutil

from colors import param
from filesystem import delete_folder, make_folder
from log import log_error, log_info, log_verbose

class Dirs:
    def __init__(self, build_dir: str, cache_dir: str, lib_dir: str, cmake_dir: str):
        self.__build_dir = build_dir
        self.__cache_dir = cache_dir
        self.__lib_dir = lib_dir
        self.__cmake_dir = cmake_dir
        self.__include_dir = f"{lib_dir}/include"
        self.__static_lib_dir = f"{lib_dir}/bin"
        self.__dynamic_lib_dir_debug = f"{build_dir}/Debug"
        self.__dynamic_lib_dir_release = f"{build_dir}/Release"
    
    def make_directories(self):
        make_folder(self.__build_dir)
        make_folder(self.__cache_dir)
        make_folder(self.__lib_dir)
        make_folder(self.__cmake_dir)
        make_folder(self.__include_dir)
        make_folder(self.__static_lib_dir)
        make_folder(self.__dynamic_lib_dir_debug)
        make_folder(self.__dynamic_lib_dir_release)
    
    def cache_file(self, dep_name: str, name: str) -> str:
        file_name = f"{self.__cache_dir}/{name}"
        self.__ensure_dir_exists_for_file(dep_name, file_name)
        return file_name
    
    def include_file(self, dep_name: str, name: str) -> str:
        file_name = f"{self.include_dir(dep_name)}/{name}"
        self.__ensure_dir_exists_for_file(dep_name, file_name)
        return file_name

    def include_dir(self, dep_name: str) -> str:
        return f"{self.__include_dir}/{dep_name}"
    
    def cmake_file(self, dep_name: str) -> str:
        return f"{self.__cmake_dir}/{dep_name}.cmake"
    
    # def copy_include_from_cache(self, name: str, is_verbose: bool, cache_src: str, include_dest: str):
    #     include_file = f"{self.__include_dir}/{include_dest}"
    #     source_file = f"{self.__cache_dir}/{cache_src}"
    #     self.__copy_file(name, is_verbose, source_file, include_file)
    
    def clean(self, clean_type: str):
        clean_type = clean_type.lower()
        if clean_type == "all":
            delete_folder(self.__build_dir)
            delete_folder(self.__lib_dir)
            delete_folder(self.__cmake_dir)
        elif clean_type == "build":
            delete_folder(self.__build_dir)
        elif clean_type == "libs":
            delete_folder(self.__lib_dir)
            delete_folder(self.__cmake_dir)
        else:
            log_error("Clean", "Unknown clean type: ", clean_type)
    
    def __ensure_dir_exists_for_file(self, dep_name: str, file_name: str):
        folder_name = os.path.dirname(file_name)
        if not os.path.exists(folder_name):
            log_info(dep_name, "Create directory: ", folder_name)
            os.makedirs(folder_name)
    
    # def __copy_file(self, name: str, is_verbose: bool, src: str, dest: str):
    #     if not os.path.exists(src):
    #         log_error(name, "File not found: ", src)
    #         exit(1)
        
    #     if os.path.exists(dest):
    #         log_verbose(name, is_verbose, "File already exists: ", dest)
    #         return
        
    #     dirname = os.path.dirname(dest)
    #     self.__make_folder(name, dirname)

    #     log_info(name, f"Copy {param(src)} -> {param(dest)}")
    #     shutil.copyfile(src, dest)
    
    # def __make_folder(self, name: str, path: str):
    #     if not os.path.exists(path):
    #         log_info(name, "Create directory: ", path)
    #         os.makedirs(path)