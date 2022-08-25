import os
import re
import shutil
import wget
import zipfile

def make_folder(path):
    if not os.path.exists(path):
        print(f"Create directory: \033[92m{path}\033[m")
        os.mkdir(path)
        return True
    return False

def delete_folder(path):
    if os.path.exists(path):
        print(f"Delete directory: \033[92m{path}\033[m")
        try:
            shutil.rmtree(path)
        except Exception as e:
            print(f"\033[91mUnable to delete directory \033[92m{path}\033[91m]: {e.message}\033[m")
            exit(1)

def download(url, file, verbose):
    if not os.path.exists(file):
        print(f"Download: \033[92m{file}\033[m")
        wget.download(url, file)
        print()
    elif verbose:
        print(f"File \033[92m{file}\033[m already exists.")

def extract_pattern_zip(zip_file: zipfile.ZipFile, pattern, base_path, is_verbose):
    for file_name in zip_file.namelist():
        match = re.match(pattern, file_name)
        if match:
            out_file_name = f"{base_path}/{match.group(1)}"
            if os.path.exists(out_file_name):
                if is_verbose:
                    print(f"File \033[92m{out_file_name}\033[m already exists.")
                continue
            data = zip_file.read(file_name)
            with open(out_file_name, "wb") as file:
                print(f"Extract \033[92m{out_file_name}\033[m")
                file.write(data)

def copy_file(src, dest, verbose):
    if not os.path.exists(src):
        print(f"\033[91mFile not found: \033[m{src}")
        exit(1)

    if not os.path.exists(dest):
        shutil.copyfile(src, dest)
    elif verbose:
        print(f"File \033[92m{dest}\033[m already exists.")
