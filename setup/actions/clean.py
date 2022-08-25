from ..dirs import PROJECT_BUILD_DIR, LIB_BUILD_DIR, LIB_BIN_DIR, LIB_INCLUDE_DIR
from ..util import delete_folder

def notify_clean(type):
    print(f"Clean: \033[92m{type}\033[m")

def clean_build():
    notify_clean("Build")
    delete_folder(PROJECT_BUILD_DIR)

def clean_libs():
    notify_clean("Libraries")
    delete_folder(LIB_BUILD_DIR)
    delete_folder(LIB_BIN_DIR)
    delete_folder(LIB_INCLUDE_DIR)

def clean(clean_type: str):
    clean_type = clean_type.lower()
    if clean_type == "build" or clean_type == "all":
        clean_build()
    if clean_type == "libs" or clean_type == "all":
        clean_libs()
