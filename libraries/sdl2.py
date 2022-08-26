import zipfile

from ...Dependency import Dependency
from ..dirs import LIB_INCLUDE_DIR, LIB_BIN_DIR, LIB_CACHE_DIR
from ..util import extract_pattern_zip

SDL2_CACHE_ZIP = f"{LIB_CACHE_DIR}/SDL2-devel-2.24.0-VC.zip"
SDL2_INCLUDE_DIR = f"{LIB_INCLUDE_DIR}/sdl2"
SDL2_BIN_DIR = f"{LIB_BIN_DIR}/sdl2"

class Sdl2(Dependency):
    def __init__(self, is_verbose):
        Dependency.__init__(self, "SDL2", is_verbose)
    
    def download(self):
        self.download_file("https://github.com/libsdl-org/SDL/releases/download/release-2.24.0/SDL2-devel-2.24.0-VC.zip", SDL2_CACHE_ZIP)

    def install(self):
        self.make_folder(SDL2_INCLUDE_DIR)
        self.make_folder(SDL2_BIN_DIR)

        with zipfile.ZipFile(SDL2_CACHE_ZIP, 'r') as zip:
            self.extract_pattern_zip(zip, r".*/include/(.+)", SDL2_INCLUDE_DIR)
            self.extract_pattern_zip(zip, r".*/lib/x64/(.+)", SDL2_BIN_DIR)
