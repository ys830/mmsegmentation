import argparse
import numpy as np
import os
import typing
import cv2
from einops import rearrange, reduce, repeat

def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help= 'filename (str): filename of image sequence')
    parser.add_argument('new_filename', help='new_filename (str): filename of target video')
    parser.add_argument('--fps', help='fps (float or int): frames per second', default=30)
    args = parser.parse_args()
    return args

def savevideo():
    args = parse_args()
    for root, dirs, files in os.walk(args.filename):
        for d in dirs:
            array = []
            templist = []
            filelist = []
            templist.append(os.path.join(root, d))
            for cla in templist:
                templist2 = []
                templist2.append(cla)
                save_file = args.new_filename
                save_name = args.new_filename + '/' + d + '.avi'
                folder = os.path.exists(save_file)
                if not folder:
                    os.mkdir(save_file)
                for cla in templist2:
                    for cla in os.listdir(cla):
                        find1 = "segmap"
                        find2 = "info"
                        if (find1 not in cla and find2 not in cla):
                            filelist.append(cla)
                    filelist.sort(key= lambda x:int(x[:-4])) # Sort the file names by numbers
                    for cla in filelist:
                        dir = os.path.join(root, d, cla)
                        img = cv2.imread(dir, -1)
                        array.append(img)
   
            array = np.stack(array)
            array = rearrange(array, 'f h w c -> c f h w', c=3)

            c , _, height, width = array.shape

            if c != 3:
                raise ValueError("savevideo expects array of shape (channels=3, frames, height, width), got shape ({})".format(", ".join(map(str, array.shape))))
            fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')
            out = cv2.VideoWriter(save_name, fourcc, args.fps, (width, height))

            for frame in array.transpose((1, 2, 3, 0)):
                frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
                out.write(frame)

if __name__ == "__main__":
   savevideo()