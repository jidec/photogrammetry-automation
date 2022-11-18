import numpy as np
import cv2
import glob
import time
from numpy.linalg import norm
import os
import imutils
from concurrent.futures import ThreadPoolExecutor

def pgOtsuMask(img,dilate_intensity=0.3,show=False):

    #scale_percent = 30
    initial_dim = [img.shape[1],img.shape[0]]

    #dim = (int(img.shape[1] * scale_percent / 100), int(img.shape[0] * scale_percent / 100))
    #img = cv2.resize(img, dim)
    img = imutils.resize(img, width=500)

    # figure out if the background is black
    lightness = np.average(norm(img, axis=2)) / np.sqrt(3)
    has_black_bg = lightness < 127
    if show:
        if has_black_bg:
            print("Detected black background")
        else:
            print("Detected white background")

    start_time = time.time()  ##################################################

    # TODO apply propor to image size
    img = cv2.GaussianBlur(img, (5, 5), 0)

    if show:
        print("Time taken for blur --- %s seconds ---" % (time.time() - start_time))
        cv2.imshow("blur",img)
        cv2.waitKey(0)
        start_time = time.time()

    start_time = time.time() ##################################################

    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    mask = cv2.threshold(img, 0, 255, #240
                           cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

    if not has_black_bg:
        mask = cv2.bitwise_not(mask)

    segment_pix_size = np.sum(img == 255)

    if show:
        print("Time taken for otsu --- %s seconds ---" % (time.time() - start_time))
        cv2.imshow("mask", mask)
        cv2.waitKey(0)
        start_time = time.time()

    k_size = int(dilate_intensity * 25)
    kernel = np.ones((k_size, k_size), np.uint8)
    mask = cv2.dilate(mask, kernel, iterations=1)

    if show:
        print("Time taken for dilate --- %s seconds ---" % (time.time() - start_time))
        cv2.imshow("dilated", mask)
        cv2.waitKey(0)
        start_time = time.time()

    #kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (20, 20))
    #mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

    #mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3)), iterations=3)
    contour, hier = cv2.findContours(mask, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_SIMPLE)

    mask = np.zeros(img.shape)
    for cnt in contour:
        cv2.drawContours(mask, [cnt], 0, 255, -1)
    mask = mask.astype(np.uint8)

    if show:
        print("Time taken for close --- %s seconds ---" % (time.time() - start_time))
        cv2.imshow("closed", mask)
        cv2.waitKey(0)
        start_time = time.time()

    # Connected components with stats.
    labels, output, stats, centroids = cv2.connectedComponentsWithStats(mask, connectivity=4)

    # remove small components for speed
    remove_barcodes_by_rectangle = False
    #remove_barcodes_by_center = False

    if remove_barcodes_by_rectangle:
        is_rectangle = []
        for l in range(labels):
            points = np.argwhere(output == l)
            rect = cv2.minAreaRect(points)
            box = cv2.boxPoints(rect)
            print(box)
            w = abs(box[1,0] - box[0,0])
            h = abs(box[2,1] - box[0,1])
            print(stats[l, cv2.CC_STAT_AREA])
            print(h*w)
            is_rectangle.append(abs(h*w - stats[l, cv2.CC_STAT_AREA]) < 10)
        non_rect_labels = [i for i, x in enumerate(is_rectangle) if x]

        # Find the largest non background component.
        # Note: range() starts from 1 since 0 is the background label.
        #max_label, max_size = max([(i, stats[i, cv2.CC_STAT_AREA]) for i in range(1, labels)], key=lambda x: x[1])
        label_areas = [(i, stats[i, cv2.CC_STAT_AREA]) for i in non_rect_labels] #range(1, labels)
        label_areas.sort(key=lambda x: x[1],reverse=True)
        top3_labels = list(zip(*label_areas[0:3]))[0]
        #print(top3_labels)
        #print(centroids)
        label_centroids = centroids[top3_labels,:]
        #print(label_centroids)
        img_mid = [np.shape(img)[1] / 2, np.shape(img)[0] / 2]
        #print(img_mid)
        centroid_dists = [sum(abs(c - img_mid)) for c in label_centroids]
        final_label = top3_labels[np.argmin(centroid_dists)]

    else:
        max_label, max_size = max([(i, stats[i, cv2.CC_STAT_AREA]) for i in range(1, labels)], key=lambda x: x[1])
        final_label = max_label

    mask = np.zeros(img.shape)
    mask[output == final_label] = 255

    if show:
        print("Time taken for comp --- %s seconds ---" % (time.time() - start_time))
        cv2.imshow("best component", mask)
        cv2.waitKey(0)

    mask = cv2.resize(mask,initial_dim)
    return(mask)

def makeMasks(folder_id, base_folder="N:/NaturalHistory/DIL/Photogrammetry/",mask_dilate_intensity=0.3,print_steps=False,show=False):
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

    if not isinstance(folder_id, list):
        folder_id = [folder_id]
    for f in folder_id:
        print("Starting folder " + f + "...")
        pg_directory = f
        pg_directory = base_folder + pg_directory + "/images"
        subdirs = [d[0] for d in os.walk(pg_directory)]

        print("Finding image paths...")
        for dir in subdirs:
            tif_paths = glob.glob(dir + '/*.tif', recursive=True)
            jpg_paths = glob.glob(dir + '/*.jpg', recursive=True)
            jpg_paths2 = glob.glob(dir + '/*.JPG', recursive=True)
            paths = tif_paths + jpg_paths + jpg_paths2

            init_start_time = time.time()

            print("Loading all images in batch...")
            start_time = time.time()
            with ThreadPoolExecutor(max_workers=32) as executor:
                imgs = list(executor.map(cv2.imread, paths))
            if print_steps: print("Time taken for img read --- %s seconds ---" % (time.time() - start_time))

            i = 0
            for img,path in tuple(zip(imgs, paths)) :
                #print(path)
                #start_time = time.time()
                #img = cv2.imread(path, cv2.IMREAD_COLOR)
                #print("Time taken for img read --- %s seconds ---" % (time.time() - start_time))

                start_time = time.time()
                mask = pgOtsuMask(img,dilate_intensity=mask_dilate_intensity)
                if print_steps: print("Time taken for full size image --- %s seconds ---" % (time.time() - start_time))

                if show:
                    scale_percent = 20
                    dim = (int(img.shape[1] * scale_percent / 100), int(img.shape[0] * scale_percent / 100))
                    resized = cv2.resize(img, dim)
                    resized_mask = pgOtsuMask(resized)
                    cv2.imshow("img", resized)
                    cv2.waitKey(0)
                    cv2.imshow("mask", resized_mask)
                    cv2.waitKey(0)

                start_time = time.time()
                cv2.imwrite(path + ".mask.png",mask)
                if print_steps: print("Time taken for write --- %s seconds ---" % (time.time() - start_time))
                i += 1
                if (i % 25) == 0:
                    print("Number of images finished:" + str(i))

        print("Finished one ID: total time taken --- %s seconds ---" % (time.time() - init_start_time))