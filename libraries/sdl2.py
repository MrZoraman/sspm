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

from zipfile import ZipFile

from Dependency import Dependency

# SDL2_CACHE_ZIP = f"{LIB_CACHE_DIR}/SDL2-devel-2.24.0-VC.zip"
# SDL2_INCLUDE_DIR = f"{LIB_INCLUDE_DIR}/sdl2"
# SDL2_BIN_DIR = f"{LIB_BIN_DIR}/sdl2"

DOWNLOAD_URL = "https://github.com/libsdl-org/SDL/releases/download/release-2.24.0/SDL2-devel-2.24.0-VC.zip"

CACHE_FILE_NAME = "SDL2-devel-2.24.0-VC.zip"


class Sdl2(Dependency):
    def __init__(self, is_verbose: bool, dirs):
        Dependency.__init__(self, "Sdl2", is_verbose, dirs)
    
    def download(self):
        path = self.cache_file(CACHE_FILE_NAME)
        self.download_file(DOWNLOAD_URL, path)
    
    def install(self):
        cache_file = self.cache_file(CACHE_FILE_NAME)
        with ZipFile(cache_file, 'r') as zip:
            self.unzip_includes(zip, r".*/include/(.+)")
            self.unzip_static_lib(zip, "SDL2-2.24.0/lib/x64/SDL2.lib", "SDL2.lib")
            self.unzip_static_lib(zip, "SDL2-2.24.0/lib/x64/SDL2main.lib", "SDL2main.lib")
            self.unzip_dynamic_lib(zip, "SDL2-2.24.0/lib/x64/SDL2.dll", "SDL2.dll")
    
    def setup_cmake(self):
        with open(self.cmake_file(), 'w') as file:
            file.write(f"set(SDL2_INCLUDE_DIR {self.include_dir()} PARENT_SCOPE)\n")
            file.write(f"set(SDL2_LIB {self.static_lib_file('SDL2.lib')} PARENT_SCOPE)\n")
            file.write(f"set(SDL2_MAIN_LIB {self.static_lib_file('SDL2main.lib')} PARENT_SCOPE)\n")

    # def install(self):
    #     self.make_folder(SDL2_INCLUDE_DIR)
    #     self.make_folder(SDL2_BIN_DIR)

    #     with zipfile.ZipFile(SDL2_CACHE_ZIP, 'r') as zip:
    #         self.extract_pattern_zip(zip, r".*/include/(.+)", SDL2_INCLUDE_DIR)
    #         self.extract_pattern_zip(zip, r".*/lib/x64/(.+)", SDL2_BIN_DIR)
