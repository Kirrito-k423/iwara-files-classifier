from tsjPython import gVal as glv
from collections import defaultdict
import time

glv._init()

glv._set("download_path", "E:\Download\Video")


#  video_name -> Game/character name -> target directory
target_base_path = "W:\\video2\\3D18"
glv._set("target_base_path", target_base_path)

genshin_directory = target_base_path + "\\" + "原神" + "\\"
bh_directory = target_base_path + "\\" + "崩坏三崩铁" + "\\"
glv._set("bh_directory", bh_directory)

glv._set("character2directory", {
    "神里凌华": genshin_directory + "凌华 Ayaka",
    "优菈": genshin_directory + "尤拉",
    "夜兰": genshin_directory + "夜阑琴团长迪西娅丽莎",
    "丽莎": genshin_directory + "夜阑琴团长迪西娅丽莎",
    "凝光": genshin_directory + "申鹤凝光",
    
    
    
    "崩三大鸭": bh_directory + "鸭鸭",
    "银狼": bh_directory + "鸭 - 但是银狼",
    "卡夫卡": bh_directory + "卡夫卡",
    

    
    
})