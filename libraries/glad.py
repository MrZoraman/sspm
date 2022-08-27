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
from Dirs import Dirs

CMAKELISTS_FILE = f"{os.path.dirname(__file__)}/cmakes/glad.cmake"
ARTIFACT_LIB_NAME = "glad.lib"

class Glad(Dependency):
    def __init__(self, is_verbose: bool, dirs: Dirs):
        Dependency.__init__(self, "glad", is_verbose, dirs)
    
    def __artifact_lib(self):
        return f"{self.lib_build_dir()}/build/Release/{ARTIFACT_LIB_NAME}"

    def build(self):
        artifact_lib = self.__artifact_lib()
        if os.path.exists(artifact_lib):
            return

        build_dir = self.lib_build_dir()
        os.system(f"python -m glad --spec gl --generator c-debug --out-path {build_dir} --reproducible")
        
        self.copy_file(CMAKELISTS_FILE, f"{self.lib_build_dir()}/CMakeLists.txt")

        build_dir = self.lib_build_dir()

        os.system(
            "cmake "
            f"-S {build_dir} "
            f"-B {build_dir}/build "
            "-G \"Visual Studio 17 2022\"")

        os.system(f"cmake --build {build_dir}/build --config Release")
    
    def install(self):
        self.copy_file(self.lib_build_file("include/glad/glad.h"), self.include_file("glad/glad.h"))
        self.copy_file(self.lib_build_file("include/KHR/khrplatform.h"), self.include_file("KHR/khrplatform.h"))
        self.copy_file(self.lib_build_file(f"build/Release/{ARTIFACT_LIB_NAME}"), self.static_lib_file(ARTIFACT_LIB_NAME))
    
    def get_libs(self):
        return [ self.static_lib_file(ARTIFACT_LIB_NAME) ]
