import os
import shutil

def renameMoveCameraImages(pg_specimen_dir):
    # for every subdir in the specimen dir
    for path, subdirs, files in os.walk(pg_specimen_dir):
        # for every file
        for name in files:
            extension = name.split(".")[-1].lower()
            # rename file as folder name + _file name + extension
            os.rename(os.path.join(path, name), os.path.join(path, os.path.basename(path) + "_" + name + "." + extension))
            # move
            shutil.move(os.path.join(path, name), os.path.join(path + "/series/noscale", name))