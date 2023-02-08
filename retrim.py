import cv2 
import numpy as np
import os
import pandas as pd
from glob import glob
from tqdm import tqdm

# check if any video need retrimming
def check_if_retrim():
    # plase change this path for store retrim information
    fp = open('trim_txt/FW/300-end.txt','a',encoding='utf-8')
    # please also change this to your own path
    vid_list = glob("./FW/*.avi")
    # plase also change the start and end in vid_list[start：end] according to your need          
    for vid in vid_list[300:]:
        cap = cv2.VideoCapture(vid)
        frame_num = int(cap.get(7))
        fps = cap.get(cv2.CAP_PROP_FPS)
        
        for i in range(frame_num):
            ret, frame = cap.read()
            cv2.imshow('frame',frame)
            k=cv2.waitKey(450)
            # press space for storing the video retriming video
            if k & 0xFF == ord(' '):               
                fp.write(vid + ' '+str(i) +' ' +str(i/fps)+"\n")
                break
            # press "n" if this video does not need retriming
            elif k & 0xFF == ord('n'):
                break  
        cap.release()
    fp.close()

def retrim():
    # please change this path to your desired output path for retrimmed video
    out_dir = './output_FW/'
    try:
        os.makedirs(out_dir)
    except:
        pass
    # plase also change this path 
    txt_list = glob("./trim_txt/FW/*.txt")
    for txt in txt_list:
        with open(txt, 'r') as f:
            for i in tqdm(f):

                vid_path, slice_frame, _ = i.split(' ')
                cap = cv2.VideoCapture(vid_path)
                frame_num = int(cap.get(7))
                frame_width = int(cap.get(3))
                frame_height = int(cap.get(4))
                output_vid = out_dir + vid_path.split('\\')[1]
                
                out = cv2.VideoWriter(output_vid,cv2.VideoWriter_fourcc(*'MJPG'), 30,
                (frame_width,frame_height))
                for i in range(frame_num):
                    ret, frame = cap.read()
                    if ret and i >int(slice_frame)+4:
                        out.write(frame)
                cap.release()
                out.release()

                
        

retrim()

# check_if_retrim()