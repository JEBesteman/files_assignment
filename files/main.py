__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

from os import mkdir, remove, listdir
import os.path
import zipfile

current_path = os.path.dirname(__file__)
# c:\Users\jebes\OneDrive\Documenten\files_assignment\files
cache_path = os.path.join(current_path, "cache")
# c:\Users\jebes\OneDrive\Documenten\files_assignment\files\cache


def clean_cache():
    try:
        mkdir(cache_path)
        print("directory cache created!")
    except FileExistsError:
        print("Emptying cache directory")
        for file in listdir(cache_path):
            remove(os.path.join(cache_path, file))


clean_cache()

zip_file_path = os.path.join(current_path, "data.zip")


def cache_zip(zip_file_path: str, cache_dir_path: str):
    with zipfile.ZipFile(zip_file_path, "r") as zip:
        zip.extractall(cache_dir_path)


cache_zip(zip_file_path, cache_path)


def cached_files():
    list_files = []
    for file in listdir(cache_path):
        list_files.append(os.path.join(cache_path, file))
    return list_files


def find_password(list_file_paths: list[str]):
    for file in list_file_paths:
        with open(file, "r") as f:
            for line in f:
                if "password" in line:
                    password = line[line.find(" ") + 1 : -1]
                    return password


print(find_password(cached_files()))
