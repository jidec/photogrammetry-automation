from createSpecimenDirectory import createSpecimenDirectory
from renameMoveCameraImages import renameMoveCameraImages
from alignExport import alignExport

#specimen_dir = "N:/NaturalHistory/DIL/Photogrammetry/2022_12/UF-IZ-123"
current_dir = "C:/Users/jacob.idec/PycharmProjects/photogrammetry-automation/photogrammetry-automation/"
specimen_dir = "../test_directories/fresh_data/UF-IZ-turtle-1"
specimen_dir = current_dir + specimen_dir
renameMoveCameraImages(specimen_dir)

# input("After dragging scale images from series/noscale to series/scale, press Enter to continue...")
# manual step - drag scale images from series/noscale to series/scale

# scale_noscale_folders_needed_1m_large: Applies scaling as 0.1 meters defined distance with large barcodes*. Images must be organized as “images” parent folder with “scale” & “noscale” subfolders.
#alignExport(specimen_dir, scale=True, use_scale_noscale_folders=True, barcode_size="large", barcode_define_distance=0.1)
