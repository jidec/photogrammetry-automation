from createSpecimenDirectory import createSpecimenDirectory
from renameMoveCameraImages import renameMoveCameraImages
from alignExport import alignExport

createSpecimenDirectory(year="2022", month_num="12", specimen_code="UF-IZ-123", num_cameras=2)

input("After adding Camera image folders to new directory, press Enter to continue...")
# manual step - drag images to Camera folders
