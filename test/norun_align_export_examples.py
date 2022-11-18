from alignExport import alignExport

current_dir = "C:/Users/jacob.idec/PycharmProjects/photogrammetry-automation/photogrammetry-automation/test_directories/fresh_data/UF-IZ-turtle"

specimen_dir = current_dir + "_subset"
# scale_noscale_folders_needed_1m_large: Applies scaling as 0.1 meters defined distance with small barcodes*. Images must be organized as “images” parent folder with “scale” & “noscale” subfolders
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=True, barcode_size="large", barcode_define_distance=0.1)

#input("Press enter to continue")
#specimen_dir = current_dir + "2"
# scale_noscale_folders_needed_05m: Applies scaling as 0.05 meters defined distance with small barcodes. Images must be organized as “images” parent folder with “scale” & “noscale” subfolders.
# alignExport(specimen_dir, scale=True, use_scale_noscale_folders=True, barcode_size="large", barcode_define_distance=0.05)

#specimen_dir = current_dir + "3"
# scale_noscale_folders_needed_noscaling: Scaling not set. Intended for when scaling would like to be done post model reconstruction. Images must be organized as “images” parent folder with “scale” & “noscale” subfolders
#alignExport(specimen_dir,scale=False,use_scale_noscale_folders=True)

input("Press enter to continue")
specimen_dir = current_dir + "4"
# all_images_1m_large: Applies scaling as 0.1 meters defined distance with large barcodes*. Images must be organized in “images” folder, no separate scale & noscale subfolders
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=False, barcode_size="large", barcode_define_distance=0.1)
input("Press enter to continue")

specimen_dir = current_dir + "5"
# all_images_1m_small: Applies scaling as 0.1 meters defined distance with small barcodes*. Images must be organized in “images” folder, no separate scale & noscale subfolders
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=False, barcode_size="small", barcode_define_distance=0.1)
input("Press enter to continue")

specimen_dir = current_dir + "6"
# all_images_05m: Applies scaling as 0.05 meters defined distance with small barcodes*. Images must be organized in “images” folder, no separate scale & noscale subfolders
alignExport(specimen_dir, scale=True, use_scale_noscale_folders=False, barcode_size="small", barcode_define_distance=0.05)
input("Press enter to continue")

specimen_dir = current_dir + "7"
# all_images_noscaling: Scale not set. Intended for when scaling would like to be done post model reconstruction. Images must be organized in “images” folder, no separate scale & noscale subfolders
alignExport(specimen_dir, scale=False, use_scale_noscale_folders=False)
input("Press enter to continue")

specimen_dir = current_dir + "8"
# aligned: Alignment already complete and saved as an RC project file. This function finishes model reconstruction after alignment. This is used with problematic models that have a hard time aligning and manual components must be used.
# alignExport(specimen_dir, load_manual_aligned=True)

specimen_dir = current_dir + "9"
# scaleCO_noscaleCO_needed: Scale image series is already aligned with scale applied and saved as an RC project, and noscale image series already aligned and exported as a component. This is used with problematic models that have a hard time aligning and very similar to the function above except this automates aligning the separate scale and noscale components
# alignExport(specimen_dir, use_scale_noscale_folders=True, load_manual_aligned=True)