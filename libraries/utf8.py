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

from Dependency import Dependency
from Dirs import Dirs

DOWNLOAD_URL = "https://raw.githubusercontent.com/sheredom/utf8.h/4e4d828174c35e4564c31a9e35580c299c69a063/utf8.h"

CACHE_FILE_NAME = "utf8.h"
INCLUDE_FILE_NAME = "utf8.h"

class Utf8(Dependency):
    def __init__(self, is_verbose: bool, dirs: Dirs):
        Dependency.__init__(self, "Utf8", is_verbose, dirs)
    
    def download(self):
        path = self.cache_file(CACHE_FILE_NAME)
        self.download_file(DOWNLOAD_URL, path)
    
    def install(self):
        cache_file_path = self.cache_file(CACHE_FILE_NAME)
        include_file_path = self.include_file(INCLUDE_FILE_NAME)
        self.copy_file(cache_file_path, include_file_path)
    
    def setup_cmake(self):
        with open(self.cmake_file(), 'w') as file:
            file.write(f"set(UTF8_INCLUDE_DIR {self.include_dir()} PARENT_SCOPE)")
