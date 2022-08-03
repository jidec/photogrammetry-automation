import subprocess

def alignExport(pg_directory, scale=True, use_scale_noscale_folders=True, load_manual_aligned=False, barcode_size="small",barcode_define_distance=0.1):
    """
        An automatic script to align and export images from a photogrammetry directory

        :param str pg_directory: the path to the photogrammetry folder for a single specimen
        :param bool scale: specify whether to scale the images by importing a /scale folder
        :param bool load_manual_aligned: specify whether to load a manually created alignment
            Requires an alignment to first be manually created and saved as "project.rcproj"
            OR two manual alignments, these are a scaled alignment saved as "scaleCO.rcproj" AND a noscale alignment saved as "noscaleCO.rcalign"
        :param str barcode_size: the size of barcodes to look for, either "small" or "large"
        :param float barcode_define_distance: the distance between the barcodes (I think?)
    """
    # throw error if load_manual_aligned is set to True and the required files for scale=True/False are not found
    # throw error if

    rc_exe = "C:\\Program Files\\Capturing Reality\\RealityCapture\\RealityCapture.exe"
    dir = pg_directory.replace("/", "\\")
    image_dir = dir + "\\images"

    if barcode_size == "small":
        barcode1 = "1x20:001a3"
        barcode2 = "1x20:001a2"
    if barcode_size == "large":
        barcode1 = "1x20:0017a"
        barcode2 = "1x20:0017b"

    # cmds starts as rc location
    cmds = [rc_exe]
    # set sequences of commands
    define_barcodes_cmds = ["-detectMarkers", "-defineDistance", barcode1, barcode2, barcode_define_distance]
    align_cmds = ["-align", "-setReconstructionRegionAuto", "-calculateNormalModel", "-selectLargestModelComponent",
                  "-invertTrianglesSelection","-removeSelectedTriangles", "-removeSelectedTriangles", "-smooth", "-unwrap", "-calculateTexture"]
    export_cmds = ["-exportSelectedModel", "morphosource\object_full.obj"]

    if use_scale_noscale_folders:
        # add the noscale folder
        cmds = cmds + ["-addFolder", image_dir + "\\noscale"]
        # align it and export the alignment
        cmds = cmds + ["-align", "-exportRegistration", "noscaleCO.rcalign"]
        # add the scale folder
        cmds = cmds + ["-addFolder", image_dir + "\\scale"]
        # detect markers, define dist, and save the scaled project
        # if scale:
        cmds = cmds + define_barcodes_cmds + ["-save", "scaleCO.rcproj"]
        # import the noscale
        cmds = cmds + ["-importComponent","noscaleCO.rcalign"]
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