from createSpecimenDirectory import createSpecimenDirectory
from renameMoveCameraImages import renameMoveCameraImages
from alignExport import alignExport

specimen_dir = "N:/NaturalHistory/DIL/Photogrammetry/2022_12/UF-IZ-123"
renameMoveCameraImages(specimen_dir)

input("After dragging scale images from series/noscale to series/scale, press Enter to continue...")
# manual step - drag scale images from series/noscale to series/scale

# scale_noscale_folders_needed_1m_large: Applies scaling as 0.1 meters defined distance with large barcodes*. Images must be organized as “images” parent folder with “scale” & “noscale” subfolders.
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=True, barcode_size="large", barcode_define_distance=0.1)

# scale_noscale_folders_needed_1m_small: Applies scaling as 0.1 meters defined distance with small barcodes*. Images must be organized as “images” parent folder with “scale” & “noscale” subfolders
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=True, barcode_size="small", barcode_define_distance=0.1)

# scale_noscale_folders_needed_05m: Applies scaling as 0.05 meters defined distance with small barcodes. Images must be organized as “images” parent folder with “scale” & “noscale” subfolders.
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=True, barcode_size="large", barcode_define_distance=0.05)

# scale_noscale_folders_needed_noscaling: Scaling not set. Intended for when scaling would like to be done post model reconstruction. Images must be organized as “images” parent folder with “scale” & “noscale” subfolders
alignExport(specimen_dir,scale=False,use_scale_noscale_folders=True)

# all_images_1m_large: Applies scaling as 0.1 meters defined distance with large barcodes*. Images must be organized in “images” folder, no separate scale & noscale subfolders
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=False, barcode_size="large", barcode_define_distance=0.1)

# all_images_1m_small: Applies scaling as 0.1 meters defined distance with small barcodes*. Images must be organized in “images” folder, no separate scale & noscale subfolders
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=False, barcode_size="small", barcode_define_distance=0.1)

# all_images_05m: Applies scaling as 0.05 meters defined distance with small barcodes*. Images must be organized in “images” folder, no separate scale & noscale subfolders
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=False, barcode_size="small", barcode_define_distance=0.05)

# all_images_noscaling: Scale not set. Intended for when scaling would like to be done post model reconstruction. Images must be organized in “images” folder, no separate scale & noscale subfolders
alignExport(specimen_dir, scale=False, use_scale_noscale_folders=False)

# aligned: Alignment already complete and saved as an RC project file. This function finishes model reconstruction after alignment. This is used with problematic models that have a hard time aligning and manual components must be used.
alignExport(specimen_dir, load_manual_aligned=True)

# scaleCO_noscaleCO_needed: Scale image series is already aligned with scale applied and saved as an RC project, and noscale image series already aligned and exported as a component. This is used with problematic models that have a hard time aligning and very similar to the function above except this automates aligning the separate scale and noscale components
alignExport(specimen_dir, use_scale_noscale_folders=True, load_manual_aligned=True)
