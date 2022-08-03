import os

# creates starting directory folders
# pg_dir is the path to the Photogrammetry folder containing year month folders
def createSpecimenDirectory(year, month_num, division_code, id, num_cameras,pg_dir="N:/NaturalHistory/DIL/Photogrammetry"):
    # add strings to get the base path
    base_path = pg_dir + "/" + year + "_" + month_num + "/UF_" + division_code + "_" + id # temp name may change
    # for every camera
    for i in range(1,num_cameras):
        # make dirs for noscale and scale for that camera
        os.makedirs(base_path + "/temp/" + "Camera" + str(i))
        # os.makedirs(base_path + "/temp/" + "Camera" + str(i) + "_scale")
    # make dir for raw
    os.makedirs(base_path + "/raw")

    # make dir for rc output files
    os.makedirs(base_path + "/rc_files")

    # make dirs for series
    os.makedirs(base_path + "/series/noscale")
    os.makedirs(base_path + "/series/scale")

    # make dirs for models
    os.makedirs(base_path + "/out_models/morphosource")
    os.makedirs(base_path + "/out_models/sketchfab")