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

import argparse
import os

from setup.util import make_folder
from setup.dirs import LIB_DIR, LIB_INCLUDE_DIR, LIB_BIN_DIR, LIB_CACHE_DIR, LIB_BUILD_DIR, PROJECT_BUILD_DIR, PROJECT_BUILD_DEBUG_DIR, PROJECT_BUILD_RELEASE_DIR
from setup.actions.clean import clean
from setup.dependencies import collect_dependencies

def run_cmake():
    os.system("cmake -S . -B build -G \"Visual Studio 17 2022\"")

def make_folders():
    make_folder(LIB_DIR)
    make_folder(LIB_CACHE_DIR)
    make_folder(LIB_INCLUDE_DIR)
    make_folder(LIB_BIN_DIR)
    make_folder(LIB_BUILD_DIR)
    make_folder(PROJECT_BUILD_DIR)
    make_folder(PROJECT_BUILD_DEBUG_DIR)
    make_folder(PROJECT_BUILD_RELEASE_DIR)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Super Simple Package Manager for C/C++")
    parser.add_argument("--clean", choices=["build", "libs", "all"], help="Completely cleans the lib directory EXCEPT lib/cache.")
    parser.add_argument("--verbose", action="store_true", help="Turn on verbose mode.")
    args = parser.parse_args()

    if args.clean:
        clean(args.clean)
        exit(0)

    make_folders()

    dependencies = collect_dependencies(args.verbose)

    for dependency in dependencies:
        dependency.log_info("Download")
        dependency.download()

        dependency.log_info("Build")
        dependency.build()

        dependency.log_info("Install")
        dependency.install()
    
    run_cmake()
