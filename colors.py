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

LOG_INFO = green("Info")
LOG_VERBOSE = gray("Verbose")
LOG_ERROR = red("Error")
