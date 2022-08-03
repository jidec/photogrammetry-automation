from old.setScaleDistanceManual import setScaleDistanceManual

root_dir = "//"
specimen_dirs = ["2022_07/UF_280569_turtle_shell_CML","2022_07/UF_280569_turtle_shell_CML2"]
specimen_dirs = [root_dir + s for s in specimen_dirs]
setScaleDistanceManual(specimen_dirs)