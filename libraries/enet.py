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
import zipfile

from Dependency import Dependency

DOWNLOAD_URL = "https://github.com/lsalzman/enet/archive/refs/tags/v1.3.17.zip"

CACHE_FILE_NAME = "enet-v1.3.17.zip"

# ENET_CACHE_ZIP = f"{LIB_CACHE_DIR}/enet-1.3.17.zip"
# ENET_BUILD_DIR = f"{LIB_BUILD_DIR}/enet-1.3.17"

# ENET_ARTIFACT_LIB = f"{ENET_BUILD_DIR}/build/release/enet.lib"

# ENET_LIB_BIN_DIR = f"{LIB_BIN_DIR}/enet"
# ENET_LIB_INCLUDE_DIR = f"{LIB_INCLUDE_DIR}/enet"
# ENET_BIN_FILE = f"{ENET_LIB_BIN_DIR}/enet.lib"

# ENET_CMAKELISTS_FILE = f"{ENET_BUILD_DIR}/CMakeLists.txt"

class Enet(Dependency):
    def __init__(self, is_verbose: bool, dirs):
        Dependency.__init__(self, "enet", is_verbose, dirs)
    
    def download(self):
        path = self.cache_file(CACHE_FILE_NAME)
        self.download_file(DOWNLOAD_URL, path)
    
    def build(self):
        pass
        # # if os.path.exists(ENET_ARTIFACT_LIB):
        # #     self.log_info("Already built.")
        # #     return
        
        # self.extract_zip(ENET_CACHE_ZIP, LIB_BUILD_DIR, ENET_BUILD_DIR)

        # # with open(ENET_CMAKELISTS_FILE, 'r') as file:
        # #     filedata = file.read()
        # #     filedata = filedata.replace("add_library(enet STATIC", "add_library(enet SHARED")
        # # with open(ENET_CMAKELISTS_FILE, 'w') as file:
        # #     file.write(filedata)

        # self.log_info("CMAKE configure")
        # os.system(
        #     "cmake "
        #     f"-S {ENET_BUILD_DIR} "
        #     f"-B {ENET_BUILD_DIR}/build "
        #     "-G \"Visual Studio 17 2022\" "
        #     "-D CMAKE_WINDOWS_EXPORT_ALL_SYMBOLS=TRUE "
        #     "-D BUILD_SHARED_LIBS=TRUE")
        
        # self.log_info("CMAKE compile")
        # os.system(f"cmake --build {ENET_BUILD_DIR}/build --config Release")
    
    # def install(self):
    #     self.make_folder(ENET_LIB_BIN_DIR)
    #     self.make_folder(ENET_LIB_INCLUDE_DIR)
    #     self.make_folder(f"{ENET_LIB_INCLUDE_DIR}/enet")

    #     self.copy_file(ENET_ARTIFACT_LIB, ENET_BIN_FILE)

    #     with zipfile.ZipFile(ENET_CACHE_ZIP, 'r') as zip:
    #         self.extract_pattern_zip(zip, r".+/(.+\.h)", f"{ENET_LIB_INCLUDE_DIR}/enet")
    
