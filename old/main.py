from old.pg_auto import createScaleManual

# quickly create directories that images and models will reside in
# createStartingDirs(root_dir="C:/Users/jacob.idec", year="2022",month_num="7",division="IZ",id="103010",num_cameras=3)

# manual step of moving images to temp folders

# rename images by adding their camera as a prefix, then move raw images into new "raw" folder and series images into new "series" folder
# renameMovePgImages(pg_specimen_dir="C:/Users/jacob.idec/2022_7/UF_IZ_103010")

# could in theory go through all date folders and look for codes
# if given just a date, then run all of the subfolders
pg_specimen_dirs = ["C:/2022_05/UF_IZ_520956"]

createScaleManual(pg_specimen_dirs)

# createModelAuto(pg_specimen_dirs)