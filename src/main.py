import config  # 加载配置
from tsjPython import gVal as glv
from input_process import inputParameters, isIceEnable
from video import Video
from tsjPython.tsjCommonFunc import *
import os

def main():
    ## icecream & input
    args=inputParameters()
    isIceEnable(args.debug)
    
    # search download directory, target video files
    files_and_folders = os.listdir(glv._get("download_path"))
    videoList = []
    for file in files_and_folders:
        ic(file)
        videoList.append(Video(glv._get("download_path"), file))
        
    passPrint("Print ready files:")
    for video in videoList:
        if video.ready == "yes":
            video.print()
            
    errorPrint("Type y to move video:")
    choice = input()
    
    if choice == "y":
        for video in videoList:
            if video.ready == "yes":
                video.move()
                # break
    else:
        yellowPrint("Skip movement.....")
    # exit()
    passPrint("Print not ready files:")
    for video in videoList:
        if video.ready == "no":
            video.print()
    


if __name__ == "__main__":
    main()