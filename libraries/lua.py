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
import zipfile

from ..Dependency import Dependency

from ..dirs import LIB_CACHE_DIR, LIB_BUILD_DIR, LIB_BIN_DIR, LIB_INCLUDE_DIR, PROJECT_BUILD_DEBUG_DIR, PROJECT_BUILD_RELEASE_DIR
from ..util import download, make_folder, extract_pattern_zip

LUA_CACHE_ZIP = f"{LIB_CACHE_DIR}/lua-5.4.4.zip"
LUA_BUILD_DIR = f"{LIB_BUILD_DIR}/lua-5.4.4"

LUA_ARTIFACT_LIB = f"{LUA_BUILD_DIR}/build/release/lua54.lib"
LUA_ARTIFACT_DLL = f"{LUA_BUILD_DIR}/build/release/lua54.dll"

LUA_CMAKE_FILE = "setup/libs/cmakes/Lua54.cmake"

LUA_LIB_BIN_DIR = f"{LIB_BIN_DIR}/lua"
LUA_LIB_INCLUDE_DIR = f"{LIB_INCLUDE_DIR}/lua"
LUA_BIN_FILE = f"{LUA_LIB_BIN_DIR}/lua54.lib"
LUA_DLL_NAME = "lua54.dll"

class Lua(Dependency):
    def __init__(self, is_verbose: bool, dirs):
        Dependency.__init__(self, "lua", is_verbose, dirs)
    
    def download(self):
        self.download_file("https://github.com/lua/lua/archive/refs/tags/v5.4.4.zip", LUA_CACHE_ZIP)
    
    def build(self):
        if os.path.exists(LUA_ARTIFACT_LIB) and os.path.exists(LUA_ARTIFACT_DLL):
            self.log_info("Already built.")

        self.extract_zip(LUA_CACHE_ZIP, LIB_BUILD_DIR, LUA_BUILD_DIR)
        self.copy_file(LUA_CMAKE_FILE, f"{LUA_BUILD_DIR}/CMakeLists.txt")

        self.log_info("CMAKE configure")
        os.system(
            "cmake "
            f"-S {LUA_BUILD_DIR} "
            f"-B {LUA_BUILD_DIR}/build "
            "-G \"Visual Studio 17 2022\" "
            "-D CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE "
            "-D BUILD_SHARED_LIBS=TRUE")
        
        self.log_info("CMAKE compile")
        os.system(f"cmake --build {LUA_BUILD_DIR}/build --config Release")

    def install(self):
        self.make_folder(LUA_LIB_BIN_DIR)
        self.make_folder(LUA_LIB_INCLUDE_DIR)

        self.copy_file(LUA_ARTIFACT_LIB, LUA_BIN_FILE)
        self.copy_file(LUA_ARTIFACT_DLL, f"{PROJECT_BUILD_DEBUG_DIR}/{LUA_DLL_NAME}")
        self.copy_file(LUA_ARTIFACT_DLL, f"{PROJECT_BUILD_RELEASE_DIR}/{LUA_DLL_NAME}")

        with zipfile.ZipFile(LUA_CACHE_ZIP, 'r') as zip:
            self.extract_pattern_zip(zip, r".*/(.+\.h)$", LUA_LIB_INCLUDE_DIR)
