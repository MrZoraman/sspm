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

from filesystem import delete_folder, make_folder
from log import log_error, log_info

class Dirs:
    def __init__(self, build_dir: str, cache_dir: str, lib_dir: str, cmake_dir: str, lib_build_dir: str):
        self.__build_dir = build_dir
        self.__cache_dir = cache_dir
        self.__lib_dir = lib_dir
        self.__cmake_dir = cmake_dir
        self.__lib_build_dir = lib_build_dir
        self.__include_dir = f"{lib_dir}/include"
        self.__static_lib_dir = f"{lib_dir}/bin"
        self.__dynamic_lib_dir_debug = f"{build_dir}/Debug"
        self.__dynamic_lib_dir_release = f"{build_dir}/Release"
    
    def make_directories(self):
        make_folder(self.__build_dir)
        make_folder(self.__cache_dir)
        make_folder(self.__lib_dir)
        make_folder(self.__cmake_dir)
        make_folder(self.__lib_build_dir)
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
    
    def static_lib_file(self, dep_name: str, name: str):
        file_name = f"{self.__static_lib_dir}/{dep_name}/{name}"
        self.__ensure_dir_exists_for_file(dep_name, file_name)
        return file_name
    
    def dynamic_lib_file_debug(self, dep_name: str, name: str):
        file_name = f"{self.__dynamic_lib_dir_debug}/{name}"
        self.__ensure_dir_exists_for_file(dep_name, file_name)
        return file_name
    
    def dynamic_lib_file_release(self, dep_name: str, name: str):
        file_name = f"{self.__dynamic_lib_dir_release}/{name}"
        self.__ensure_dir_exists_for_file(dep_name, file_name)
        return file_name
    
    def lib_build_dir(self, dep_name: str) -> str:
        folder_name = f"{self.__lib_build_dir}/{dep_name}"
        if not os.path.exists(folder_name):
            log_info(dep_name, "Create directory: ", folder_name)
            os.makedirs(folder_name)
        return folder_name
    
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
