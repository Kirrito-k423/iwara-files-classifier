from tsjPython import gVal as glv
from collections import defaultdict
import time

glv._init()

# glv._set("download_path", "E:\Download\Video")
glv._set("download_path", "G:\Video\iwaraTmp")
# glv._set("download_path", "E:\Download")


#  video_name -> Game/character name -> target directory
target_base_path = "W:\\video2\\3D18"
glv._set("target_base_path", target_base_path)

genshin_directory = target_base_path + "\\" + "原神" + "\\"
bh_directory = target_base_path + "\\" + "崩坏三崩铁" + "\\"
anime_directory = target_base_path + "\\" + "iwaraAnime" + "\\"
iwara_directory = target_base_path + "\\" + "iwara" + "\\"
miku_directory = iwara_directory + "miku"
glv._set("bh_directory", bh_directory)

glv._set("character2directory", {
    # Genshin
    "神里凌华": genshin_directory + "凌华 Ayaka",
    "优菈": genshin_directory + "尤拉",
    "夜兰": genshin_directory + "夜阑琴团长迪西娅丽莎",
    "丽莎": genshin_directory + "夜阑琴团长迪西娅丽莎",
    "凝光": genshin_directory + "申鹤凝光",
    "申鹤": genshin_directory + "申鹤凝光",
    "心海": genshin_directory + "心海 kokomi",
    
    # bh3
    "崩三大鸭": bh_directory + "鸭鸭",
    "银狼": bh_directory + "鸭 - 但是银狼",
    "卡夫卡": bh_directory + "卡夫卡",
    "爱莉希雅": bh_directory + "爱莉",
    
    "Kangxi": iwara_directory + "Kangxi",
    "约尔": anime_directory + "约尔",
    "老婆光": target_base_path + "\\" + "异度之刃2" 

    
    
})

glv._set("typeNoname2directory", {
    "原神":genshin_directory+"1 合集",
    "崩坏三":bh_directory + "1 合集",
    "崩坏星穹铁道":bh_directory + "1 合集",
})

glv._set("typeIgnorename2directory", {  
    "碧蓝航线": iwara_directory + "碧蓝航线 (Azur Lane)",
    "碧蓝档案": iwara_directory + "KK 碧蓝档案 Blue Archive",
    "深空之眼": iwara_directory + "深空之眼",
    "幻塔": iwara_directory + "幻塔",
    "战双帕弥什": iwara_directory + "战双",
    "公主链接": iwara_directory + "公主链接",
    "少女前线": iwara_directory + "少女前线2云图",
    "赛马娘": iwara_directory + "赛马娘",
    "机动战队": iwara_directory + "机动战队",
    "FF14": iwara_directory,
    "明日方舟": iwara_directory,
    
    # anime
    "鬼灭之刃": anime_directory + "鬼灭之刃",
    "FGO": anime_directory + "FGO",
    "咒术回战": anime_directory,
    "死神": anime_directory,
    "间谍过家家": anime_directory,
    "租借女友": anime_directory,
    
    "虚拟歌姬": miku_directory,
    
    
    "Other": iwara_directory + "杂"

    
    
})