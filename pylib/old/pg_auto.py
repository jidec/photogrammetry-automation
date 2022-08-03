import json
import subprocess
import os
import shutil
import glob
import time

# parses date folders to all subdirs
def parseSpecimenDirs(pg_specimen_dirs):
    for index, dir in enumerate(pg_specimen_dirs):
        if not dir.contains("UF_IZ"):
            subdirs = [f.path for f in os.scandir(dir)]
            # remove date dir
            pg_specimen_dirs.remove(dir)
            # add specimen dirs
            pg_specimen_dirs.add(subdirs)

# creates starting directory folders
# pg_dir is the path to the Photogrammetry folder containing year month folders
def createSpecimenDirectory(pg_dir, year, month_num, division, id, num_cameras):
    # add strings to get the base path
    base_path = pg_dir + "/" + year + "_" + month_num + "/UF_" + division + "_" + id # temp name may change
    # for every camera
    for i in range(1,num_cameras):
        # make dirs for noscale and scale for that camera
        os.makedirs(base_path + "/temp/" + "Camera" + str(i))
        os.makedirs(base_path + "/temp/" + "Camera" + str(i) + "_scale")
    # make dir for raw
    os.makedirs(base_path + "/raw")
    # make dirs for series
    os.makedirs(base_path + "/series/noscale")
    os.makedirs(base_path + "/series/scale")

# renames images to ensure no duplicate names by adding the name of the camera folder before each image name
# i.e. 943818 gets renamed to Camera1_943818.jpg
# pg_specimen_dir is the path to the specimen folder i.e. UF_IZ_01
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

# creates a new raw folder in <year-month>/<specimen-code> folder and moves raw images to it
# pg_specimen_dir is the path to the specimen folder i.e. UF_IZ_01
def moveRawImages(pg_specimen_dir):
    # make a new dir to hold raw files
    os.mkdir(pg_specimen_dir + "/raw")
    for path, subdirs, files in os.walk(pg_specimen_dir):
        # for every file
        for name in files:
            extension = name.split(".")[-1].lower()
            if extension == "cs2":
                # move .cs2 files to raw folder
                shutil.move(os.path.join(path, name), os.path.join(path + "/raw/", name))

# likewise, move all non-raw images to a new folder called series
# pg_specimen_dir is the path to the specimen folder i.e. UF_IZ_01
def moveSeriesImages(pg_specimen_dir):
    color_checker = sorted(glob.glob(pg_specimen_dir + "/*.jpg"), key=os.path.getctime)[0]
    for path, subdirs, files in os.walk(pg_specimen_dir):
        # for every file
        for name in files:
            extension = name.split(".")[-1].lower()
            if extension != "cs2":
                # move non cs2 files
                # to series/noscale if not a scale image
                if "_scale" in name:
                    shutil.move(os.path.join(path, name), os.path.join(path + "/series/scale/", name))
                else:
                    shutil.move(os.path.join(path, name), os.path.join(path + "/series/noscale/", name))

# combines image folder functions
#def renameMovePgImages(pg_specimen_dir):
#    renameCameraImages(pg_specimen_dir)
#    moveRawImages(pg_specimen_dir)
#    moveSeriesImages(pg_specimen_dir)

def test(pg_specimen_dir):
    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"

# sets scale markers for listed specimens
def setScaleMarkersAuto(pg_specimen_dirs):
    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"
    # for each specimen dir
    for dir in pg_specimen_dirs:
        # fix dir string for cmd
        dir = dir.replace("/", "\\")

        subprocess.Popen(rc_exe + " -newScene" +
                         " -addFolder " + "\"" + dir + "\\series\\scale" + "\"" +
                         " -detectMarkers" +
                        " -save" + "\"" + dir + "\\markers.rcproj" + "\"")

def setScaleDistanceManual(pg_specimen_dirs):
    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"
    # for each specimen dir
    for dir in pg_specimen_dirs:
        # fix dir string for cmd
        dir = dir.replace("/", "\\")
        # load marker project
        subprocess.run(rc_exe + " -load" + " " + "\"" + dir + "\\markers.rcproj" + "\"")
        # close out of this after saving as distances.rcproj

#def setScaleFinalAuto(pg_specimen_dirs):
#    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"
    # for each specimen dir
#    for dir in pg_specimen_dirs:
        # fix dir string for cmd
#        dir = dir.replace("/", "\\")
        # load marker project
#        subprocess.run(rc_exe + " -load" + " " + "\"" + dir + "\\distances.rcproj" + "\"")

def alignNoScaleAuto(pg_specimen_dirs):
    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"
    # for each dir
    for dir in pg_specimen_dirs:

        dir = dir.replace("/", "\\")

        subprocess.Popen(rc_exe + " -setInstanceName " + "rc")
        subprocess.Popen(rc_exe + " -delegateTo rc" + " -newScene")
        time.sleep(2)
        # open RC and create a new scene
        subprocess.call(rc_exe + " -newScene")
        # add the series folder containing images
        subprocess.call(rc_exe + " -addFolder " + dir + "/series/noscale")
        # align
        subprocess.call(rc_exe + " -align")

        # export the point cloud
        subprocess.call(rc_exe + " -exportRegistration " + dir + "/noscale.rcalign")

def createModelAuto(pg_specimen_dirs,out_model_name):
    # set the location of the RealityCapture program
    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"

    # for each dir
    for dir in pg_specimen_dirs:
        dir = dir.replace("/", "\\")

        subprocess.Popen(rc_exe + " -setInstanceName " + "rc")
        subprocess.Popen(rc_exe + " -delegateTo rc" + " -newScene")
        time.sleep(2)
        # open RC and create a new scene
        subprocess.call(rc_exe + " -newScene")
        # add the series folder containing images
        subprocess.call(rc_exe + " -addFolder " + dir + "/series/noscale")
        # align
        subprocess.call(rc_exe + " -align")

        # export the point cloud
        subprocess.call(rc_exe + " -exportRegistration " + dir + "/noscale.rcalign")

        # align no scale, export component
        # set scale, align scaled image set, save as rcproj to get imported for automatic
        # alignSetScaleManual

        subprocess.call(rc_exe + " -newScene")

        # load scale proj
        subprocess.call(rc_exe + " -load " + dir + "/scale.rcproj")

        # import component
        subprocess.call(rc_exe + " -importComponent " + dir + "/noscale.rcalign")
        # align again
        subprocess.call(rc_exe + " -align")

        # set auto reconstruction region - create box of area of interest for meshing
        subprocess.call(rc_exe + " -setReconstructionRegionAuto")
        # calculate normal model - mesh
        subprocess.call(rc_exe + " -calculateNormalModel")
        # find largest component, invert selection to get smaller components, and remove those
        subprocess.call(rc_exe + " -selectLargestModelComponent")
        subprocess.call(rc_exe + " -invertTrianglesSelection")
        subprocess.call(rc_exe + " -removeSelectedTriangles")

        # remove noise (current default setting of program)
        subprocess.call(rc_exe + " -smooth")
        # prepare texture
        subprocess.call(rc_exe + " -unwrap")
        subprocess.call(rc_exe + " -calculateTexture")

        # export model obj
        subprocess.call(rc_exe + " -exportSelectedModel \"" + dir + "/" + out_model_name + "-full.obj" + "\"")

        # simplify medium
        subprocess.call(rc_exe + " -simplify " + "1000000") # will pull in xml files

        # reproject texture from full to simplified (model names from application)
        subprocess.call(rc_exe + " -reprojectTexture " + "1000000")  # will pull in xml files
        # export model obj
        subprocess.call(rc_exe + " -exportSelectedModel \"" + dir + "/" + out_model_name + "-simplified.obj" + "\"")
        # save and close project
        subprocess.call(rc_exe + " -save " + "rc.rcproj")
        subprocess.call(rc_exe + " -quit")
        # load next

# old function doing everyone at once
def createScaleManual(pg_specimen_dirs):
    # set the location of the RealityCapture program
    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"

    # for each specimen dir
    for dir in pg_specimen_dirs:
        dir = dir.replace("/", "\\")
        # open RC and create a new scene
        #command = rc_exe + " -newScene"
        #os.system('cmd /k ' + "\"" + command + "\"")

        subprocess.Popen(rc_exe + " -setInstanceName " + "rc")
        subprocess.Popen(rc_exe + " -delegateTo rc" + " -newScene")
        time.sleep(2)
        # add the series folder containing scale images
        subprocess.Popen(rc_exe + " -delegateTo rc" + " -addFolder " + "\"" + dir + "\\series\\scale" + "\"")
        time.sleep(2)
        # detect markers
        subprocess.Popen(rc_exe + " -delegateTo rc" + " -detectMarkers")

        # alternatively, should split this to save marker.rcproj for all specimens, prepareMarkers()
        # then load all marker projects one at a time and define distances and save as distances.rcproj, prepareManualDistances())
        # then run alignments and save as another function prepareScale()
        input("Press ENTER after distance has been manually defined to continue with alignment...")

        # align
        subprocess.Popen(rc_exe + " -delegateTo rc" + " -align")

        # save the RC project for the noscaled
        subprocess.call(rc_exe + " -delegateTo rc" + " -save " + dir + "/scale.rcproj")

# drag in non scaled images
# --NewScene
# --AddFolder
# --align
# --detectMarkers (params.xml)
# --defineDistance
# --AddFolder no scaled
# --align
# -setReconstructionRegionAuto -calculateNormalModel -selectLargestModelComponent -invertTrianglesSelection
# -removeSelectedTriangles -smooth -unwrap -calculateTexture -simplify -exportSelectedModel "%~dp0model\object_500k.obj" -save "%~dp0object.rcproj"

## Required starting directory structure - Photogrammetry/*year_*month#/UF_*division_*id/Camera1, Camera2...

# output of aligning scale images - save as a reality capture project - open project