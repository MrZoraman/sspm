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

import zipfile

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

    # def install(self):
    #     self.make_folder(SDL2_INCLUDE_DIR)
    #     self.make_folder(SDL2_BIN_DIR)

    #     with zipfile.ZipFile(SDL2_CACHE_ZIP, 'r') as zip:
    #         self.extract_pattern_zip(zip, r".*/include/(.+)", SDL2_INCLUDE_DIR)
    #         self.extract_pattern_zip(zip, r".*/lib/x64/(.+)", SDL2_BIN_DIR)
