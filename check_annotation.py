import numpy as np
import cv2
import pandas as pd
import os
from tqdm import tqdm

# please replace with your own path
trim_csv =r"C:\Users\jingy\Parkinson\Codes\data_trim.csv"
df= pd.read_csv(trim_csv)

def check_trim_csv(df):
    for index, row in df.iterrows():
        # make sure column name is corrects(without extra space)
        vid_path = row.get("Video_Path")
        FW_Start, FW_End = row.get("FW_Start"), row.get("FW_End")
        BW_Start, BW_End = row.get("BW_Start"), row.get("BW_End")
        vid_path = vid_path.replace('"','')
        #check if video exist
        try:
            os.path.exists(vid_path)
        except:
            print("File not exists:", vid_path)
        #check if the label is correct
        if not pd.isnull(FW_Start) and not pd.isnull(FW_End):
            try:
                assert FW_Start < FW_End
                assert FW_End-FW_Start < 20
            except:
                print("Incorrect Time", index)
                
        if not pd.isnull(BW_Start) and not pd.isnull(BW_End):
            try:
                assert BW_Start < BW_End
                assert BW_End-BW_Start < 20
            except:
                print("Incorrect Time", index)
    print("All files have been checked!")
check_trim_csv(df)