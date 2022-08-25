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
    parser = argparse.ArgumentParser(description="Various project setup activities including but not limited to downloading and building dependencies.")
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
