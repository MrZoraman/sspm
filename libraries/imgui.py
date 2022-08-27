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

from Dependency import Dependency

DOWNLOAD_URL = "https://github.com/ocornut/imgui/archive/refs/tags/v1.88.zip"
CACHE_FILE_NAME = "imgui-v1.88.zip"
CMAKELISTS_FILE = f"{os.path.dirname(__file__)}/cmakes/imgui.cmake"
ARTIFACT_LIB_NAME = "imgui.lib"

class Imgui(Dependency):
    def __init__(self, is_verbose: bool, dirs):
        Dependency.__init__(self, "imgui", is_verbose, dirs)
    
    def download(self):
        path = self.cache_file(CACHE_FILE_NAME)
        self.download_file(DOWNLOAD_URL, path)
    
    def __artifact_lib(self):
        return f"{self.lib_build_dir()}/imgui-1.88/build/Release/{ARTIFACT_LIB_NAME}"

    def build(self):
        artifact_file_dll = self.__artifact_lib()
        if os.path.exists(artifact_file_dll):
            return

        self.extract_cache_zip_to_build_dir(CACHE_FILE_NAME)

        self.copy_file(CMAKELISTS_FILE, f"{self.lib_build_dir()}/imgui-1.88/CMakeLists.txt")
        
        build_dir = f"{self.lib_build_dir()}/imgui-1.88"

        os.system(
            "cmake "
            f"-S {build_dir} "
            f"-B {build_dir}/build "
            "-G \"Visual Studio 17 2022\"")

        os.system(f"cmake --build {build_dir}/build --config Release")
    
    def install(self):
        self.copy_file(self.lib_build_file("imgui-1.88/imconfig.h"), self.include_file("imconfig.h"))
        self.copy_file(self.lib_build_file("imgui-1.88/imgui.h"), self.include_file("imgui.h"))
        self.copy_file(self.lib_build_file("imgui-1.88/imgui_internal.h"), self.include_file("imgui_internal.h"))
        self.copy_file(self.lib_build_file("imgui-1.88/imstb_rectpack.h"), self.include_file("imstb_rectpack.h"))
        self.copy_file(self.lib_build_file("imgui-1.88/imstb_textedit.h"), self.include_file("imstb_textedit.h"))
        self.copy_file(self.lib_build_file("imgui-1.88/imstb_truetype.h"), self.include_file("imstb_truetype.h"))
        
        self.copy_file(self.lib_build_file(f"imgui-1.88/build/Release/{ARTIFACT_LIB_NAME}"), self.static_lib_file(ARTIFACT_LIB_NAME))

    def setup_cmake(self):
        with open(self.cmake_file(), 'w') as file:
            file.write(f"set(IMGUI_INCLUDE_DIR {self.include_dir()} PARENT_SCOPE)\n")
            file.write(f"set(IMGUI_LIB {self.static_lib_file(ARTIFACT_LIB_NAME)} PARENT_SCOPE)\n")
