import os
import shutil

def copy_from_to_recursive(path_to_static, path_to_public):
    if os.path.exists(path_to_public):
        shutil.rmtree(path_to_public)

    os.mkdir(path_to_public)
    for file in os.listdir(path_to_static):
        path_to_static_dir = path_to_static+'/'+file
        path_to_public_dir = path_to_public+'/'+file
        if os.path.isfile(path_to_static_dir):
            shutil.copy(path_to_static_dir, path_to_public_dir)
        else:
            copy_from_to_recursive(path_to_static_dir, path_to_public_dir)
            