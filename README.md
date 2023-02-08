# Folder Structure

``` 
├── csv:                     where all .csv format files store 
├── data:                    store all the video dataset data
├── gt_build:                codes for final ground truth validation and mapping
├── trim_txt:                this all .txt file for retrimming the trimmed videos.
├── check_annoation.py:      check all the labeled time stamps in the "trim_csv" is correct 
├── Checks.ipynb:            a sample code when I build other file, please ignore for now
├── combine_vid.py:          copy all trimmed video and check if any video is invalid 
├── flawed-clean.py:         watch every FW/BW video and check if any is flawed
├── multi_video_trim.py:     trimmed all the videos and store in subject manner
├── retrim.py:               watch every FW/BW video and check if any needs retrimming
├── single_video_trim.ipynb: a sample code for video trimming, please ignore for now
├── stat_analysis.ipynb:     run some stat analysis 

```
# File Execution
    1. Run check_annoation.py 
    2. Run multi_video_trim.py
    3. Run combine_vid.py 
    4. Manually split FW/BW video into two separate folder. like "videos_dir/FW" or "videos_dir/BW"
    5. Run retrim.py for both FW/BW videos.
    6. Run flawed-clean.py for both retrimmed FW/BW videos

# Common conda commands:
activate env:
```
conda activate env_name
```
    2. deactivate env(make sure ur in actiavted env):
        ```
        conda decativate
        ``` 
    3. see all installed conda env:
        ```
        conda info --envs
        ``` 
    4. see all pakages installed within a env:
        ```
        conda list
        ``` 
    5. install arbitrary packages:
        ```
        pip install package_name
        ``` 
