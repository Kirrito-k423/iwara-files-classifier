from tsjPython import gVal as glv
from collections import defaultdict
import time

glv._init()

glv._set("download_path", "E:\Download\Video")


#  video_name -> Game/character name -> target directory
target_base_path = "W:\\video2\\3D18"
glv._set("target_base_path", target_base_path)

genshin_directory = target_base_path + "\\" + "原神" + "\\"

glv._set("character2directory", {
    "神里凌华": genshin_directory + "凌华 Ayaka",
    "优菈": genshin_directory + "尤拉",
    
    
})