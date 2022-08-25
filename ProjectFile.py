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
from setup.colors import param

PROJECT_FILE_PATHS = ["sspm.yml", "sspm.yaml", "../sspm.yml", "sspm.yaml"]

def find_project_file():
    project_file_path = None
    for possible_file_location in PROJECT_FILE_PATHS:
        if os.path.exists(possible_file_location):
            project_file_path = possible_file_location
    
    if not project_file_path:
        return None

    print(f"Found project file at: {param(project_file_path)}")
    
    with open(project_file_path, 'r') as file:
        raw_project_file = yaml.load(file, Loader=yaml.FullLoader)
    
    return ProjectFile()

class ProjectFile:
    pass