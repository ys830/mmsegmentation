import argparse
import os
import cv2
import numpy as np
from tqdm import tqdm

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('img_pth', help='train image file path')
    args = parser.parse_args()
    return args

def mean():
    args = parse_args()
    tr_img_files = [file for file in os.listdir(args.img_pth)\
            if os.path.splitext(file)[1] in [".png"]]

    totalRGB = np.asarray([0],dtype=np.int64)
    totalVar = np.asarray([0],dtype=np.float64)
    meanRGB = np.asarray([0],dtype=np.float64)
    varRGB = np.asarray([0],dtype=np.float64)

    for img_file in tqdm(tr_img_files,desc="calculating mean",mininterval=0.1):
        img_file = os.path.join(args.img_pth,img_file)
        img = cv2.imread(img_file,-1)
        totalRGB += np.sum(img)
    img_size = img.shape[:2]
    total_pixels = img_size[0]*img_size[1]*len(tr_img_files)
    meanRGB = totalRGB/total_pixels

    for img_file in tqdm(tr_img_files,desc="calculating var",mininterval=0.1):
        img_file = os.path.join(args.img_pth,img_file)
        img = cv2.imread(img_file,-1)
        totalVar += np.sum((img-meanRGB)**2)
    varRGB = np.sqrt(totalVar/total_pixels)

    print("img_size:{}x{}".format(img_size[1],img_size[0]))
    print("meanRGB:{}".format(meanRGB))
    print("stdRGB:{}".format(varRGB))

    return (img_size[1],img_size[0]), meanRGB, varRGB

if __name__ == "__main__":
    mean()