User guide:
1. Click a script in example_scripts to open it in PyCharm
2. It will say "No Python interpreter configured for this project", click "Use..." to fix this
3. Edit the script to your liking
4. Run the script by right-clicking it then clicking "Run..."

If making more complex workflows, copy the example_scripts to your own personal folder, then make changes

alignExport parameters guide - see examples in example_scripts
"""
        An automatic script to align and export images from a photogrammetry directory

        :param str OR list folder_id: the path to the photogrammetry folders formatted like so "2022-11/UF_Herp_104033"
            Can be a single path OR a list of paths like ["2022-11/UF_Herp_104033", "2022-11/UF_Herp_330234"]
        :param bool scale: specify whether to scale the images by importing a /scale folder
        :param bool load_manual_aligned: specify whether to load a manually created alignment
            Requires either:
                1. an alignment to first be manually created and saved as "project.rcproj"
                2. two manual alignments, these are a scaled alignment saved as "scaleCO.rcproj"
                    AND a noscale alignment saved as "noscaleCO.rcalign"
        :param str barcode_size: the size of barcodes to look for, either "small" or "large"
            Will throw an error if the size barcodes are not found in the images
        :param float barcode_define_distance: the known distance between the barcodes
        :param int simplify_xml_iters: if greater than 0, model is simplified using a required "simplificationParams.xml"
                file in the pg_directory which contains a percent to simplify by in the key "mvsFltTargetTrisCountRel"
            Then, simplify_xml_iters specifies how many times to simplify by this percent in sequence.
            For example, if "mvsFltTargetTrisCountRel" is 50% and simplify_xml_iters is 3, the model is simplified
                to 50% of the original, then 25%, then 12.5% - only the final one (12.5% here) is saved
"""

makeMasks parameters guide - see examples in example_scripts
"""
            An automatic script to align and export images from a photogrammetry directory

            :param str OR list folder_id: the path to the photogrammetry folders formatted like so "2022-11/UF_Herp_104033"
                Can be a single path OR a list of paths like ["2022-11/UF_Herp_104033", "2022-11/UF_Herp_330234"]
            :param float mask_dilate_intensity: the amount to "puff out" masks
                Lower values make masks tighter to specimens but can lead to missed portions
            :param bool print_steps: specify whether to print detailed steps
            :param bool show: specify whether to show masked images for testing
                Shown images must be exited before next image will appear
"""