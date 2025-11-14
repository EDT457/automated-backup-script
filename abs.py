import os
import shutil

def backup_files(source, dest):
    if not os.path.isdir(dest):
        os.makedirs(dest, exist_ok=True)
    if os.path.isdir(source):
        for file in os.listdir(source):
            if os.path.isfile(os.path.join(source, file)):
                source_file = os.path.join(source, file)
                dest_file = os.path.join(dest, file)
                shutil.copy2(source_file,dest_file)
            else:
                backup_files(os.path.join(source, file), os.path.join(dest, file))
 