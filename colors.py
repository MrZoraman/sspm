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

COLOR_RESET = "\033[m"
COLOR_MAGENTA = "\033[95m"
COLOR_GRAY = "\033[90m"
COLOR_GREEN = "\033[92m"
COLOR_CYAN = "\033[96m"
COLOR_RED = "\033[91m"

COLOR_PARAM = COLOR_CYAN

def param(text):
    return f"{COLOR_PARAM}{text}{COLOR_RESET}"

def magenta(text):
    return f"{COLOR_MAGENTA}{text}{COLOR_RESET}"

def green(text):
    return f"{COLOR_GREEN}{text}{COLOR_RESET}"

def gray(text):
    return f"{COLOR_GRAY}{text}{COLOR_RESET}"

def red(text):
    return f"{COLOR_RED}{text}{COLOR_RESET}"
