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

DOWNLOAD_URL = "https://github.com/glfw/glfw/releases/download/3.3.8/glfw-3.3.8.bin.WIN64.zip"
CACHE_FILE_NAME = "glfw-3.3.8.bin.WIN64.zip"
STATIC_LIB_NAME = "glfw3.lib"

class Glfw(Dependency):
    def __init__(self, is_verbose: bool, dirs):
        Dependency.__init__(self, "glfw", is_verbose, dirs)
    
    def download(self):
        path = self.cache_file(CACHE_FILE_NAME)
        self.download_file(DOWNLOAD_URL, path)
    
    def install(self):
        cache_file = self.cache_file(CACHE_FILE_NAME)
        with ZipFile(cache_file, 'r') as zip:
            self.unzip_includes(zip, r"glfw-3.3.8.bin.WIN64/include/(GLFW/.+.h)")
            self.unzip_static_lib(zip, f"glfw-3.3.8.bin.WIN64/lib-vc2022/{STATIC_LIB_NAME}")

    def get_libs(self):
        return [ self.static_lib_file(STATIC_LIB_NAME) ]
