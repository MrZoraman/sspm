from Dependency import Dependency
from Dirs import Dirs

# from ..Dependency import Dependency
# from ..dirs import LIB_INCLUDE_DIR, LIB_CACHE_DIR

# UTF8_INCLUDE_DIR = f"{LIB_INCLUDE_DIR}/utf8"
# UTF8_CACHE_FILE = f"{LIB_CACHE_DIR}/utf8.h"
# UTF8_INCLUDE_FILE = f"{UTF8_INCLUDE_DIR}/utf8.h"

DOWNLOAD_URL = "https://raw.githubusercontent.com/sheredom/utf8.h/4e4d828174c35e4564c31a9e35580c299c69a063/utf8.h"

class Utf8(Dependency):
    def __init__(self, is_verbose: bool, dirs: Dirs):
        Dependency.__init__(self, "Utf8", is_verbose)
        self.__dirs = dirs
        self.__cache_file = dirs.cache_file("utf8.h")
    
    def download(self):
        self.download_file(DOWNLOAD_URL, self.__cache_file)
    
#     def download(self):
#         self.download_file("https://raw.githubusercontent.com/sheredom/utf8.h/4e4d828174c35e4564c31a9e35580c299c69a063/utf8.h", UTF8_CACHE_FILE)

#     def install(self):
#         self.make_folder(UTF8_INCLUDE_DIR)
#         self.copy_file(UTF8_CACHE_FILE, UTF8_INCLUDE_FILE)
