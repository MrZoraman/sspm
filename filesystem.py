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

from log import log_error, log_info

def make_folder(path):
    if not os.path.exists(path):
        log_info("Project", "Create directory: ", path)
        os.makedirs(path)
        return True
    return False

def delete_folder(path):
    if os.path.exists(path):
        log_info("Project", "Delete directory: ", path)
        try:
            shutil.rmtree(path)
        except Exception as e:
            log_error("Project", "Unable to delete directory: ", path)
            exit(1)