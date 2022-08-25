import os
import zipfile

from ..Dependency import Dependency
from ..dirs import LIB_INCLUDE_DIR, LIB_BIN_DIR, LIB_CACHE_DIR, LIB_BUILD_DIR, PROJECT_BUILD_DEBUG_DIR, PROJECT_BUILD_RELEASE_DIR

UV_CACHE_ZIP = f"{LIB_CACHE_DIR}/libuv-v1.44.2.zip"
UV_BUILD_DIR = f"{LIB_BUILD_DIR}/libuv-1.44.2"

UV_ARTIFACT_LIB = f"{UV_BUILD_DIR}/build/release/uv.lib"
UV_ARTIFACT_DLL = f"{UV_BUILD_DIR}/build/release/uv.dll"

UV_LIB_BIN_DIR = f"{LIB_BIN_DIR}/uv"
UV_LIB_INCLUDE_DIR = f"{LIB_INCLUDE_DIR}/uv"
UV_BIN_FILE = f"{UV_LIB_BIN_DIR}/uv.lib"
UV_DLL_NAME = "uv.dll"

class Uv(Dependency):
    def __init__(self, is_verbose):
        Dependency.__init__(self, "libuv", is_verbose)

    def download(self):
        self.download_file("https://github.com/libuv/libuv/archive/refs/tags/v1.44.2.zip", UV_CACHE_ZIP)

    def build(self):
        if os.path.exists(UV_ARTIFACT_LIB) and os.path.exists(UV_ARTIFACT_DLL):
            self.log_info("Already built.")
            return

        self.extract_zip(UV_CACHE_ZIP, LIB_BUILD_DIR, UV_BUILD_DIR)

        self.log_info("CMAKE configure")
        os.system(
            "cmake "
            f"-S {UV_BUILD_DIR} "
            f"-B {UV_BUILD_DIR}/build "
            "-G \"Visual Studio 17 2022\" " 
            "-D LIBUV_BUILD_TESTS=OFF "
            "-D LIBUV_BUILD_BENCH=OFF")
        
        self.log_info("CMAKE compile")
        os.system(f"cmake --build {UV_BUILD_DIR}/build --config Release")
    
    def install(self):
        self.make_folder(UV_LIB_BIN_DIR)
        self.make_folder(UV_LIB_INCLUDE_DIR)
        self.make_folder(f"{UV_LIB_INCLUDE_DIR}/uv")
        self.copy_file(UV_ARTIFACT_LIB, UV_BIN_FILE)
        self.copy_file(UV_ARTIFACT_DLL, f"{PROJECT_BUILD_DEBUG_DIR}/{UV_DLL_NAME}")
        self.copy_file(UV_ARTIFACT_DLL, f"{PROJECT_BUILD_RELEASE_DIR}/{UV_DLL_NAME}")

        with zipfile.ZipFile(UV_CACHE_ZIP, 'r') as zip:
            self.extract_pattern_zip(zip, r".*/include/(.+\.h)", UV_LIB_INCLUDE_DIR)
