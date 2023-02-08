import glob
import os
import numpy as np
import cv2
from tqdm import tqdm
from shutil import copyfile

# please replace this path
original_path='./data/dataset_with_state/**/*.avi'
path_list=glob.glob(original_path)
# please replace this path
target_path='./data/combined_with_state/'

if not os.path.exists(target_path): os.makedirs(target_path)
print("Total Video Num:{0}".format(len(path_list)))
for vid_path in tqdm(path_list):
    video = cv2.VideoCapture(vid_path)
    try:
        ret, frame = video.read()
        assert ret
        vid_name_list=vid_path.split("\\")
        output_vid =  target_path + vid_name_list[1]+'_'+vid_name_list[2]
        copyfile(vid_path, output_vid)
        
        # print(output_vid)
    except:
        print("Invalid trimmed video: ", vid_path)
                
    
