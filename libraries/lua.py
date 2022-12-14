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
from zipfile import ZipFile

from Dependency import Dependency

DOWNLOAD_URL = "https://github.com/lua/lua/archive/refs/tags/v5.4.4.zip"
CACHE_FILE_NAME = "lua-v5.4.4.zip"
ARTIFACT_LIB_NAME = "lua54.lib"
CMAKELISTS_FILE = f"{os.path.dirname(__file__)}/cmakes/Lua54.cmake"

class Lua(Dependency):
    def __init__(self, is_verbose: bool, dirs):
        Dependency.__init__(self, "lua", is_verbose, dirs)
    
    def download(self):
        path = self.cache_file(CACHE_FILE_NAME)
        self.download_file(DOWNLOAD_URL, path)
    
    def __artifact_dll(self):
        return f"{self.lib_build_dir()}/lua-5.4.4/build/Release/{ARTIFACT_DLL_NAME}"
    
    def __artifact_lib(self):
        return f"{self.lib_build_dir()}/lua-5.4.4/build/Release/{ARTIFACT_LIB_NAME}"

    def build(self):
        artifact_file_dll = self.__artifact_dll()
        if os.path.exists(artifact_file_dll):
            return

        self.extract_cache_zip_to_build_dir(CACHE_FILE_NAME)

        self.copy_file(CMAKELISTS_FILE, f"{self.lib_build_dir()}/lua-5.4.4/CMakeLists.txt")
        
        build_dir = f"{self.lib_build_dir()}/lua-5.4.4"

        os.system(
            "cmake "
            f"-S {build_dir} "
            f"-B {build_dir}/build "
            "-G \"Visual Studio 17 2022\"")

        os.system(f"cmake --build {build_dir}/build --config Release")
    
    def install(self):
        cache_file = self.cache_file(CACHE_FILE_NAME)
        with ZipFile(cache_file, 'r') as zip:
            self.unzip_includes(zip, r".*/(.+\.h)$")

        lib_file_src = self.__artifact_lib()
        self.copy_file(lib_file_src, self.static_lib_file(ARTIFACT_LIB_NAME))
    
    def get_libs(self):
        return [ self.static_lib_file(ARTIFACT_LIB_NAME) ]
