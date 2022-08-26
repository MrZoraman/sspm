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

from filesystem import delete_folder, make_folder
from colors import param, red

class Dirs:
    def __init__(self, build_dir: str, cache_dir: str, lib_dir: str):
        self.__build_dir = build_dir
        self.__cache_dir = cache_dir
        self.__lib_dir = lib_dir
    
    def make_directories(self):
        make_folder(self.__build_dir)
        make_folder(self.__cache_dir)
        make_folder(self.__lib_dir)
    
    def clean(self, clean_type: str):
        clean_type = clean_type.lower()
        if clean_type == "all":
            delete_folder(self.__build_dir)
            delete_folder(self.__lib_dir)
        elif clean_type == "build":
            delete_folder(self.__build_dir)
        elif clean_type == "libs":
            delete_folder(self.__lib_dir)
        else:
            print(f"{red('Unkonwn clean type:')} {param(clean_type)}")