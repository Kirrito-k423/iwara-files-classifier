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
    directory = glv._get("download_path")
    files_and_folders = [file for file in os.listdir(directory) if file.endswith(".mp4")]
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
    
    errorPrint("Type x to cancel classify one by one:")
    choice = input()
    if not choice == "x":
        for video in videoList:
            if video.ready == "no":
                video.print()
                
                yellowPrint("Type Keyword to classify(1. empty to Other type and move 2. \"s\" to skip):")
                Keyword = input()
                if Keyword == 's':
                    None
                elif Keyword:
                    video.regexInfo(Keyword)
                    video.print()
                    
                    errorPrint("Type x to cancel move video:")
                    choice = input()
                    if choice == "x":
                        yellowPrint("Cancel move video")
                    else:
                        video.move()
                else:
                    video.regexInfo("Orz")
                    video.print()
                    video.move()
                # break
    else:
        yellowPrint("Skip classify one by one.....")


if __name__ == "__main__":
    main()