import numpy as np
import cv2
import pandas as pd
import os
from tqdm import tqdm
import math


# the code for trimming a single video
def trim_vid(vid_path,output_vid,start,end):
    # define some video property 
    cap = cv2.VideoCapture(vid_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    frame_num = int(cap.get(7))

    # calculate the frame to start and end 
    start_frame = math.ceil(start * fps)
    end_frame = math.ceil(end * fps)

    # define out put video
    out = cv2.VideoWriter(output_vid,cv2.VideoWriter_fourcc(*'MJPG'), 30,
    (frame_width,frame_height))

    # set the video to start frame
    cap.set(1,start_frame)

    # load and save the frames
    for i in range(end_frame-start_frame):

      ret, frame = cap.read()
      if ret == True: 
        out.write(frame)

    cap.release()
    out.release()

    cv2.destroyAllWindows()


# main function for batch video trimming based on collected "data_trim.csv"
def trim_videos(df, trim_vid_dir="data/test_del"):
    for index, row in tqdm(df.iterrows(),desc="Trimming videos... slow... please wait"):
        # Please make sure column name is corrects(without extra space)
        vid_path = row.get("Video_Path")
        vid_path = vid_path.replace('"','')
        # get time stamp for FW and BW gait 
        FW_Start, FW_End = row.get("FW_Start"), row.get("FW_End")
        BW_Start, BW_End = row.get("BW_Start"), row.get("BW_End")
        # define some output directories and video_name
        # get the current path and concat with the target path for trimmed videos
        data_dir = os.path.join(os.getcwd(), trim_vid_dir)
         # make folder for each subject
        subject_dir = os.path.join(data_dir, vid_path.split("\\")[4])
        # try to make folder 
        try:
            os.makedirs(subject_dir)
        # if already exist stop creating and continue
        except:
            pass
        # print if any video is in .MTS format
        if vid_path.endswith(".MTS"):
            print(vid_path)
            continue

        # double check that all data points' time stamp is valid
        if not pd.isnull(FW_Start) and not pd.isnull(FW_End):
            output_vid = os.path.join(subject_dir, row["Time"]+"_"+row.get("ON or OFF")+"_"+"FW_"+row["R1 or R2"]+"_"+str(FW_Start)+"_.avi")
            if not os.path.exists(output_vid):
                trim_vid(vid_path,output_vid,FW_Start,FW_End)
            
        # double check that all data points' time stamp is valid
        if not pd.isnull(BW_Start) and not pd.isnull(BW_End):
            output_vid = os.path.join(subject_dir, row["Time"]+"_"+row.get("ON or OFF")+"_"+"BW_"+row["R1 or R2"]+"_"+str(BW_Start)+"_.avi")
            if not os.path.exists(output_vid):
                trim_vid(vid_path,output_vid,BW_Start,BW_End)

if __name__ == '__main__':
    # please replace with your own path
    trim_csv =r"C:\Users\jingy\Parkinson\Codes\csv\data_trim.csv"
    df= pd.read_csv(trim_csv)
    # please replace this path
    trim_videos(df, trim_vid_dir="data/test_del")
