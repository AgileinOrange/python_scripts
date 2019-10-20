#Following are the steps we are going to do:
#1) define variables for source folder and target folder
#2) os.walk through the source folder
#3) use string.replace() to get the correct paths of sub folders in the target folder
#4) if the sub folders do not exist, create them
#5) for all the files under the current sub folder, remove them first. Then create or move from the source folder to the target folder depending upon the flag operation


import os
import shutil

root_src_dir = os.path.join('.','source')
root_target_dir = os.path.join('.','target')

operation= 'copy' # 'copy' or 'move'

for src_dir, dirs, files in os.walk(root_src_dir):
    dst_dir = src_dir.replace(root_src_dir, root_target_dir)
    if not os.path.exists(dst_dir):
        os.mkdir(dst_dir)
    for file_ in files:
        src_file = os.path.join(src_dir, file_)
        dst_file = os.path.join(dst_dir, file_)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        if operation is 'copy':
            shutil.copy(src_file, dst_dir)
        elif operation is 'move':
            shutil.move(src_file, dst_dir)
