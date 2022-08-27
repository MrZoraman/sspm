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

from Project import find_project
from log import log_error

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Super Simple Package Manager for C/C++")
    parser.add_argument("--clean", choices=["build", "libs", "all"], help="Completely cleans the lib directory EXCEPT lib/cache.")
    parser.add_argument("--verbose", action="store_true", help="Turn on verbose mode.")
    args = parser.parse_args()

    project = find_project(args.verbose)
    if not project:
        log_error("Project", "Unable to find project file!")
        exit(0)

    if args.clean:
        project.clean(args.clean)
        exit(0)

    project.make_directories()

    project.setup_dependencies()
