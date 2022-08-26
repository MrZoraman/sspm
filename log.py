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

from colors import gray, green, magenta, param, red

LOG_INFO = green("Info")
LOG_VERBOSE = gray("Verbose")
LOG_ERROR = red("Error")

def log_info(name: str, message: str, param_1: str = ''):
    print(f"[{magenta(name)}] [{LOG_INFO}] {message}{param(param_1)}")

def log_verbose(name: str, is_verbose: bool, message: str, param_1: str = ''):
    if is_verbose:
        print(f"[{magenta(name)}] [{LOG_VERBOSE}] {message}{param(param_1)}")

def log_error(name: str, message: str, param_1: str = ''):
    print(f"[{magenta(name)}] [{LOG_ERROR}] {message}{param(param_1)}")