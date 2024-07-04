import os

import shutil

def list_directory(path):
    print(os.listdir(path))
    return os.listdir(path)
    
def check_if_path_exists(path):
    print(f'path {path}: {os.path.exists(path)}')
    return os.path.exists(path)
    
def main():
    path_to_static = "/home/szeri/git/boot.dev/static-site-generator/static"
    path_to_public = "/home/szeri/git/boot.dev/static-site-generator/public"
    # list_directory("/home/szeri/git/boot.dev")
    # check_if_path_exists("/home/szeri/git/boot.dev")    
    if check_if_path_exists(path_to_public):
        shutil.rmtree(path_to_public)
    else:
        os.mkdir(path_to_public)
        content = list_directory(path_to_static)
        print(content)
        for file in content:
            print(file)
            shutil.copy(path_to_static+'/'+file, path_to_public)
    
if __name__ == "__main__":
    main()