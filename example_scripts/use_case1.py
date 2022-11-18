from alignExport import alignExport
#"2022_11/UF_UF_244450"
#["2022_11/UF_UF_24445330", "2022_11/UF_UF_244450"]

# make directories if necessary
alignExport(folder_id=["automation_tests/UF-IZ-turtle_subset", "automation_tests/UF-IZ-turtle_subset2"], scale=True, use_scale_noscale_folders=True, barcode_size="large", barcode_define_distance=0.1)