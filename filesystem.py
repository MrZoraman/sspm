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

def make_folder(path):
    if not os.path.exists(path):
        print(f"Create directory: \033[92m{path}\033[m")
        os.makedirs(path)
        return True
    return False

def delete_folder(path):
    if os.path.exists(path):
        print(f"Delete directory: \033[92m{path}\033[m")
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(f"\033[91mUnable to delete directory \033[92m{path}\033[91m]: {e.message}\033[m")
            exit(1)