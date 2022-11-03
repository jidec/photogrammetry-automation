import os
import shutil

def renameMoveCameraImages(pg_specimen_dir):
    # for every subdir in the specimen dir
    base_path = pg_specimen_dir + "/temp"
    for path, subdirs, files in os.walk(base_path):
        # for every file
        for name in files:
            extension = name.split(".")[-1].lower()
            # rename file as folder name + _file name + extension
            new_name = os.path.basename(path) + "_" + name + "." + extension
            os.rename(os.path.join(path, name), os.path.join(path, new_name))
            # move
            shutil.move(os.path.join(path, new_name), os.path.join(pg_specimen_dir + "/series/noscale", new_name))