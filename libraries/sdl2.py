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
            self.unzip_static_lib(zip, "SDL2-2.24.0/lib/x64/SDL2.lib")
            self.unzip_static_lib(zip, "SDL2-2.24.0/lib/x64/SDL2main.lib")
            self.unzip_dynamic_lib(zip, "SDL2-2.24.0/lib/x64/SDL2.dll")
    
    def get_libs(self):
        return [ self.static_lib_file('SDL2.lib'), self.static_lib_file('SDL2main.lib') ]
