import json
import subprocess
import os
import shutil
import glob
import time

# sets scale markers for listed specimens
def setScaleDistanceManual(pg_specimen_dirs):
    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"

    # make into a list if not one already
    if not isinstance(pg_specimen_dirs, list):
        pg_specimen_dirs = [pg_specimen_dirs]

    # for each specimen dir
    for dir in pg_specimen_dirs:
        # fix dir string for cmd
        dir = dir.replace("/", "\\")
        subprocess.Popen(rc_exe + " -newScene" +
                         " -addFolder " + "\"" + dir + "\\series\\scale" + "\"" +
                         " -detectMarkers")