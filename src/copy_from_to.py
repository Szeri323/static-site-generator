import os
import shutil

def copy_from_to(path_to_static, path_to_public):
    if os.path.exists(path_to_public):
        shutil.rmtree(path_to_public)
    else:
        os.mkdir(path_to_public)
        for file in os.listdir(path_to_static):
            if file.endswith('.md'):
                continue
            path_to_static_dir = path_to_static+'/'+file
            path_to_public_dir = path_to_public+'/'+file
            if os.path.isfile(path_to_static_dir):
                shutil.copy(path_to_static_dir, path_to_public_dir)
            else:
                copy_from_to(path_to_static_dir, path_to_public_dir)
                # os.mkdir(path_to_public+'/'+file)
                # dir_content = os.listdir(path_to_static_dir)
                # for file_in_dir in dir_content:
                #     if os.path.isfile(path_to_static_dir+'/'+file_in_dir):
                #         shutil.copy(path_to_static_dir+'/'+file_in_dir, path_to_public_dir)
    
def main():
    path_to_static = "/home/szeri/git/boot.dev/static-site-generator/static"
    path_to_public = "/home/szeri/git/boot.dev/static-site-generator/public"
    copy_from_to(path_to_static, path_to_public)  
    
    
if __name__ == "__main__":
    main()