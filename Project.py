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
import yaml

from colors import param, red
from Dependency import Dependency
from Dirs import Dirs

PROJECT_FILE_PATHS = ["sspm.yml", "sspm.yaml", "../sspm.yml", "sspm.yaml"]

def find_project(is_verbose: bool):
    project_file_path = None
    for possible_file_location in PROJECT_FILE_PATHS:
        if os.path.exists(possible_file_location):
            project_file_path = possible_file_location
    
    if not project_file_path:
        return None

    print(f"Found project file at: {param(project_file_path)}")
    
    with open(project_file_path, 'r') as file:
        raw_project_data = yaml.load(file, Loader=yaml.FullLoader)
    
    return Project(raw_project_data, is_verbose)

class Project:
    def __init__(self, raw_project_data, is_verbose: bool):
        self.__dirs = Dirs(
            build_dir=raw_project_data["Dirs"]["Build"],
            cache_dir=raw_project_data["Dirs"]["Cache"],
            lib_dir=raw_project_data["Dirs"]["Lib"],
            lib_build_dir=raw_project_data["Dirs"]["LibBuild"])
        self.__dependency_name_list = raw_project_data["Dependencies"]
        self.__is_verbose = is_verbose

    def clean(self, clean_type: str):
        self.__dirs.clean(clean_type)

    def make_directories(self):
        self.__dirs.make_directories()
    
    def __get_dependency(self, dependency_name: str) -> Dependency:
        dependency_name = dependency_name.lower()

        if dependency_name == "utf8":
            from libraries.utf8 import Utf8
            return Utf8(self.__is_verbose, self.__dirs)
        
        if dependency_name == "sdl2":
            from libraries.sdl2 import Sdl2
            return Sdl2(self.__is_verbose, self.__dirs)
        
        if dependency_name == "enet":
            from libraries.enet import Enet
            return Enet(self.__is_verbose, self.__dirs)
        
        if dependency_name == "uv":
            from libraries.uv import Uv
            return Uv(self.__is_verbose, self.__dirs)
        
        if dependency_name == "lua":
            from libraries.lua import Lua
            return Lua(self.__is_verbose, self.__dirs)
        
        if dependency_name == "gsl":
            from libraries.gsl import Gsl
            return Gsl(self.__is_verbose, self.__dirs)
        
        if dependency_name == "glm":
            from libraries.glm import Glm
            return Glm(self.__is_verbose, self.__dirs)
        
        if dependency_name == "glad":
            from libraries.glad import Glad
            return Glad(self.__is_verbose, self.__dirs)
        
        if dependency_name == "glfw":
            from libraries.glfw import Glfw
            return Glfw(self.__is_verbose, self.__dirs)
        
        if dependency_name == "imgui":
            from libraries.imgui import Imgui
            return Imgui(self.__is_verbose, self.__dirs)

        if dependency_name == "imgui-opengl3":
            from libraries.imgui_opengl3 import Imgui_Opengl3
            return Imgui_Opengl3(self.__is_verbose, self.__dirs)
        
        if dependency_name == "imgui-glfw":
            from libraries.imgui_glfw import Imgui_Glfw
            return Imgui_Glfw(self.__is_verbose, self.__dirs)

        return None
    
    def setup_dependencies(self):
        include_dirs = []
        static_libs = []

        for dependency_name in self.__dependency_name_list:
            dependency = self.__get_dependency(dependency_name)
            if not dependency:
                print(f"{red('Unable to find dependency:')} {param(dependency_name)}")
                continue
            
            dependency.download()
            dependency.build()
            dependency.install()

            include_dirs.append(dependency.include_dir())

            for dependency_lib in dependency.get_libs():
                if not dependency_lib in static_libs:
                    static_libs.append(dependency_lib)

            include_dirs_str = ""
            for include_dir in include_dirs:
                include_dirs_str = include_dirs_str + " " + os.path.abspath(include_dir)
            
            static_libs_str = ""
            for static_lib in static_libs:
                static_libs_str = static_libs_str + " " + os.path.abspath(static_lib)
            
            with open("sspm.cmake", 'w') as file:
                file.write(f"set(SSPM_INCLUDE_DIRS {include_dirs_str})\n")
                file.write(f"set(SSPM_LIBS {static_libs_str})\n")
