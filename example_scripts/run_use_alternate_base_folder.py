from makeMasks import makeMasks
from alignExport import alignExport

# the "base_folder" parameter defaults to "N:/NaturalHistory/DIL/Photogrammetry/" if you don't supply this param,
# but you can also supply it to look for folder ids inside a different path such as "N:/NaturalHistory/DIL/2D/"
makeMasks(folder_id="2022_11/UF_UF_244450",base_folder="N:/NaturalHistory/DIL/2D/",mask_dilate_intensity=0.2)
alignExport(folder_id="2022_11/UF_UF_244450", base_folder="N:/NaturalHistory/DIL/2D/", scale=True, use_scale_noscale_folders=True, barcode_size="large", barcode_define_distance=0.1)