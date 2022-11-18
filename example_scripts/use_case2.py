from alignExport import alignExport

# make directories if necessary
# smaller scalebar
alignExport(folder_id=["automation_tests/UF-IZ-turtle_subset","automation_tests/UF-IZ-turtle_subset2"], scale=True, use_scale_noscale_folders=True, barcode_size="small", barcode_define_distance=0.1)