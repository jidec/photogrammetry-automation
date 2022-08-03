
def getSpecimenDirs(pg_dir, years_seasons=None,specimen_names=None):

    if years_seasons is None and specimen_names is None:
        print("no years-seasons or specimen names passed: finished")

    # find all names in years_seasons
    if years_seasons is None and specimen_names is not None:
        print("no years-seasons or specimen names passed: finished")