import subprocess

def alignExport(pg_directory, scale=True, use_scale_noscale_folders=True, load_manual_aligned=False, barcode_size="large",barcode_define_distance=0.1,
                simplify_xml_iters=3): #simplify_tris=[5000,1000,500]):
    """
        An automatic script to align and export images from a photogrammetry directory

        :param str pg_directory: the path to the photogrammetry folder for a single specimen
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
                to 50% of the original, then 25%, then 12.5%
    """
    # throw error if load_manual_aligned is set to True and the required files for scale=True/False are not found

    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"
    dir = pg_directory.replace("/", "\\")
    image_dir = dir + "\\series"

    if barcode_size == "small":
        barcode1 = "1x20:001a3"
        barcode2 = "1x20:001a2"
    if barcode_size == "large":
        barcode1 = "1x20:0017a"
        barcode2 = "1x20:0017b"

    # cmds starts as rc location
    cmds = [rc_exe]
    # set sequences of commands
    # processing - opERATION failed on calculate normal model
    define_barcodes_cmds = ["-detectMarkers", "-defineDistance", barcode1, barcode2, barcode_define_distance]
    align_cmds = ["-align", "-setReconstructionRegionAuto", "-calculateNormalModel", "-selectLargestModelComponent",
                  "-invertTrianglesSelection", "-removeSelectedTriangles", "-smooth", "-unwrap", "-calculateTexture"]
    export_cmds = ["-exportSelectedModel", pg_directory + "/morphosource/object_full.obj"]

    model_n = 4
    for t in range(simplify_xml_iters):
        model_string = "Model " + str(model_n)
        target = pg_directory + "/sketchfab/obj_reduced_" + str(t) + str(model_n) +".obj" #.replace('/','\\')
        export_cmds = export_cmds + ["-simplify",pg_directory + "/simplifyParameters.xml","-unwrap","-reprojectTexture","Model 3",model_string,"-exportSelectedModel",target]
        model_n += 1

    if use_scale_noscale_folders:
        # add the noscale folder
        cmds = cmds + ["-addFolder", image_dir + "\\noscale"]
        # align it and export the alignment
        cmds = cmds + ["-align", "-exportRegistration", image_dir + "/noscaleCO.rcalign"]
        # add the scale folder
        cmds = cmds + ["-addFolder", image_dir + "\\scale"]
        # detect markers, define dist, and save the scaled project
        # if scale:
        cmds = cmds + define_barcodes_cmds + ["-save", image_dir + "/scaleCO.rcproj"]
        # import the noscale
        cmds = cmds + ["-importComponent", image_dir + "/noscaleCO.rcalign"]
        # align
        cmds = cmds + align_cmds
        # export
        cmds = cmds + export_cmds
    else:
        # add the images folder
        cmds = cmds + ["-addFolder", image_dir]
        # define barcodes
        cmds = cmds + define_barcodes_cmds
        # align
        cmds = cmds + align_cmds
        # export
        cmds = cmds + export_cmds

    # add escape sequenced parantheses
    cmds = ["\"" + str(s) + "\"" if not str(s).startswith("-") else str(s) for s in cmds]
    cmd = ' '.join(cmds)

    print("Running constructed command: " + cmd)

    # run the set command
    subprocess.Popen(cmd)