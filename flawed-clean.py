import cv2 
import numpy as np
import os
import pandas as pd
from glob import glob

# retrim_dict ={'Filename':[], 'Trim_start':[],'Convert2Sec':[]}
# file = r'D:\test.txt'
# please replace this path
fp = open('test_del.txt','a',encoding='utf-8')
# please replace this path
vid_list = glob("./data/output_BW/*.avi")

for vid in vid_list:
    cap = cv2.VideoCapture(vid)
    frame_num = int(cap.get(7))
    fps = cap.get(cv2.CAP_PROP_FPS)
    
    for i in range(frame_num):
        ret, frame = cap.read()
        cv2.imshow('frame',frame)
        k=cv2.waitKey(35)
        if k & 0xFF == ord(' '):               

            fp.write(vid +"\n")
            break
        elif k & 0xFF == ord('n'):
            break  

    cap.release()
    # break
fp.close()
