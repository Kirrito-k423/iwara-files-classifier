
from tsjPython.tsjCommonFunc import *
from tsjPython import gVal as glv
from tsjPython import tsjCLI 
import re

class Video():
    
    game2characters = {
        
        # game
        "原神":["神里凌华","雷电将军","甘雨","娜维娅","丝柯克",
              "刻晴","优菈","八重神子","夜兰","凝光","莫娜","丽莎","妮露","克洛琳德",
              "芙宁娜","申鹤","胡桃","纳西达","心海","北斗","芭芭拉","云堇","闲云","宵宫"], 
        "崩坏三": ["爱莉希雅","崩三大鸭","薇塔","琪亚娜","幽兰戴尔","希儿","大月下","格蕾修","素裳","希娜狄雅","阿波尼亚"],
        "崩坏星穹铁道": ["卡夫卡","符玄","三月七","镜流","银狼","姬子","艾丝妲",
                   "桂乃芬","阮梅","霍霍","黑塔","托帕","花火","流萤","黑天鹅","希露瓦"],
        "绝区零":["妮可"],
        
        # other game publisher
        "碧蓝航线":["Tashkent","能代","光辉","Bremerton","埃吉尔","圣路易斯"],
        "碧蓝档案":["晴奈","Plana","杏山千纱","カリン","尤卡","飛鳥馬トキ","一之濑明日奈","銀鏡伊織"],
        "幻塔":["陵光","凛夜"],
        "战双帕弥什":["含英"],    
        "深空之眼":["英招"],    
        "明日方舟":[],    
        "公主链接":["臭鼬"],
        "赛马娘":["Umamusume","东海帝皇","北部玄驹","成田大进"],
        "机动战队":["陇"],
        "少女前线":["黛烟"],
        
        
        "异度之刃2":["老婆光"],
        "FF14":["踊り子ビ"],
        
        # Anime
        "鬼灭之刃":["甘露寺蜜璃","蝴蝶忍"],    
        "FGO":["玛修","间桐樱"],
        "咒术回战":["釘崎野薔薇"],
        "死神":["松本乱菊"],
        "租借女友":["水原千鹤"],
        "间谍过家家":["约尔","夜帷"],
        "古力特":["寶多六花"],
        "更衣人偶":["喜多川"],
        
        
        # vtuber
        "虚拟歌姬":["结月缘","Kangxi","miku","兎田ぺこら","弱音"],    
        
        "Other":["Orz"],
        
    }
    
    gameNickname = \
    {
        "原神":["Genshin","ヒルチャール","Liyue","璃月","Inazuma","稻妻","绿刑者"],    
        "崩坏三":["女武神","bh3","honkai_impact_3"],    
        "绝区零":["ZZZ"],
        "幻塔":["塔"],    
        "崩坏星穹铁道":["StarRail","Star Rail"],    
        "少女前线":["Frontline"],    
        "战双帕弥什":["zhan shuang","pamish"],    
        "赛马娘":["ウマ娘"],
        "碧蓝航线":["Azur","Azur Lane","AzurLane","グアム","关岛","慰安", "艦隊",],
        "碧蓝档案":["Blue"],
        "明日方舟":["Arknights"],    
        
        # anime
        "死神":["Bleach"],
        
                
    }
    
    characterNickname = {
        
        # mihoyo
        "雷电将军": ["Raiden Shogun","Raiden", "雷电", "将军" ,"雷電將軍","雷電将軍"],
        "神里凌华": ["Ayaka","神里","綾華"],
        "星铁鸭": [],
        "崩三大鸭": ["大鸭鸭","布洛妮娅","Bronya","鸭"],
        "卡夫卡":["kafka","Kafka","Kafuka","卡芙卡"],
        "黑塔":["Herta"],
        "幽兰戴尔":["呆鹅","幽兰黛尔"],
        "爱莉希雅":["爱莉","elysia","人之律者"],
        "符玄":[],
        "素裳":[],
        "艾丝妲":[],
        "希露瓦":[],
        "霍霍":["huohuo","藿藿"],
        "三月七":["March 7th"],
        "镜流":["jingliu"],
        "格蕾修":["Griseo"],
        "阿波尼亚":["Aponia"],
        "大月下":["月下"],
        "希娜狄雅":[],
        "心海":["kokomi"],
        "甘雨":["Ganyu"],
        "优菈":["Eula"],
        "克洛琳德":["CHLORIDE"],
        "八重神子":["八重","神子","Yae Miko","Miko","狐狸"],
        "刻晴":["Keqing","玉衡星"],
        "芙宁娜":["芙卡洛斯","Furina","芙芙"],
        "凝光":[],
        "申鹤":["Shenhe"],
        "阮梅":["Ruan_Mei","阮","Ruanmei"],
        "夜兰":[],
        "莫娜":["Mona","モナ"],
        "花火":[],
        "丽莎":["Lisa"],
        "妮露":[],
        "桂乃芬":["小桂子"],
        "娜维娅":["Navia"],
        "纳西达":["Nahida"],
        "北斗":[],
        "宵宫":[],
        "闲云":[],
        "芭芭拉":[],
        "云堇":["云师傅"],
        "薇塔":[],
        "银狼":["Silver Wolf"],
        "流萤":["等你回来","流螢","流莹","Firefly"],
        "黑天鹅":["Black Swan"],
        "托帕":["topaz"],
        "胡桃":[],
        "姬子":[],
        "希儿":["Seele"],
        "琪亚娜":["Kiana"],
        "丝柯克":["Skirk"],
        
        "妮可":["Nicole"],
        
        # other game publisher
        "老婆光":["Mythra"],
        "陵光":[],
        "凛夜":["Linye"],
        "含英":["Hanying"],
        "英招":["YingZhao"],
        "臭鼬":["キャル","Karyl","凯露"],
        "陇":["朧"],
        "踊り子ビ":[],
        "黛烟":["雷蒙"],
        
        ## Blue Archive
        "Plana":["プラナ"],
        "晴奈":[],
        "一之濑明日奈":[],
        "銀鏡伊織":[],
        "杏山千纱":["杏山千纱","Kazusa","カズサ"],
        "カリン":["角楯","角楯花梨"],
        "尤卡":["ユウカ"],
        "飛鳥馬トキ":[],
        
    
        
        ## Azur
        "Tashkent":[],
        "能代":["Noshiro"],
        "光辉":[],
        "埃吉尔":[],
        "圣路易斯":["圣姨"],
        "Bremerton":[],
        
        ## 赛马娘
        "Umamusume":["小巧圓繭"],
        "东海帝皇":["Tokai Teio","トウカイテイオー"],
        "北部玄驹":["Kitasan Black","玄驹"],
        "成田大进":[],
        
        # Anime character
        "甘露寺蜜璃":["Mitsuri Kanroji","Mitsuri"],
        "玛修":[],
        "釘崎野薔薇":["Nobara","Kugisaki"],
        "松本乱菊":["Rangiku Matsumoto"],
        "蝴蝶忍":["shinobu","kocho"],
        "约尔":["Yor Forger","福杰"],
        "夜帷":[],
        "水原千鹤":["水原"],
        "间桐樱":[],
        "寶多六花":[],
        "喜多川":[],
        
        # 虚拟歌姬
        "结月缘":["ゆかりさん","Yuzuki Yukari"],
        "Kangxi":["康熙"],
        "洛天依":["天依"],
        "miku":["初音","haku"],
        "弱音":[],
        "兎田ぺこら":["兎田","ぺこら"],
        
        
        "Orz":[],
        "":[],
    }
    
    
    songName = [
        "Spicy",
        "Savage",
        "Dream of you",
        "Rollin",
        "badguy",
        "WADADA",
        "NumberNine",
        "Number 9",
        "queencard"
    ]
    
    def __init__(self,path,filename):
        self.old_path = path
        self.filename = filename
        # set 
        [self.game, self.character, self.song] = ["","",""]
        self.regexInfo(filename)
        
        
        
        
    def regexInfo(self,filename):
        # directly recognize game/charater/song name from filename
        for official_game, nicklist in self.gameNickname.items():
            # ic(official_game, nicklist)
            if re.search(official_game,filename):
                self.game=official_game
                ic("Match game {} : {} in {}".format(self.game, official_game, filename))
                break
            for nickname in nicklist:
                if re.search(nickname,filename,re.I):
                    self.game=official_game
                    ic("Match game {} : {} in {}".format(self.game, nickname, filename))
                    break
                
        for official_charater, nicklist in self.characterNickname.items():
            # ic(official_charater, nicklist)
            for nickname in nicklist:
                if re.search(nickname,filename,re.I):
                    self.character=official_charater
                    ic("Match character {} : {} in {}".format(self.character, nickname, filename))
                    break
            if self.character:
                break
            if re.search(official_charater,filename,re.I):
                self.character=official_charater
                ic("Match character {} : {} in {}".format(self.character, official_charater, filename))
                break
                
        for song in self.songName:
            if re.search(song,filename,re.I):
                self.song=song
                ic("Match song {} : {} in {}".format(self.song, song, filename))
                break
        
        # If no game name, find game name using the character name
        if not self.game:
            if self.character:
                for game, characterList in self.game2characters.items():
                    if self.character in characterList:
                        self.game = game
        
        if self.character or self.game:
            self.ready = "yes"
        else:
            self.ready = "no"
        
        self.target_path = self.findTarget()
            
        
    def findTarget(self):
        # if gVal set , use it
        if self.character in glv._get("character2directory"):
            return glv._get("character2directory")[self.character]
        elif self.game in glv._get("typeNoname2directory") and not self.character:
            return glv._get("typeNoname2directory")[self.game]
        elif self.game in glv._get("typeIgnorename2directory"):
            return glv._get("typeIgnorename2directory")[self.game]
        elif self.game == "崩坏星穹铁道" or self.game == "崩坏三":
            return glv._get("bh_directory")+self.character
        else:
            # or return base + game + charactor
            return glv._get("target_base_path")+"\\"+\
                    self.game+"\\"+\
                    self.character
        
    def print(self):
        if self.ready == "yes":
            passPrint(self.filename) 
            yellowPrint("Game \t\t{}\nCharacter \t{}\nSong\t\t{}".format(self.game, self.character, self.song))
            yellowPrint("Target path: \t{}".format(self.target_path))
        else:
            print(self.filename)
        if not self.game:
            errorPrint("game is empty")
        if not self.character:
            errorPrint("character is empty")
        if not tsjCLI.checkFileExists(self.target_path):
            errorPrint("target_path not existed")
        
        
    def move_file_with_progress(self, src_file, dst_file):
        import shutil
        from tqdm import tqdm
        import os
        # 获取文件大小
        file_size = os.path.getsize(src_file)

        # 设置每次读取的块大小
        buffer_size = 8 * 1024 * 1024  # 4MB

        # 使用 tqdm 创建进度条
        with tqdm(total=file_size, unit='B', unit_scale=True, desc=f'Moving {src_file}') as pbar:
            with open(src_file, 'rb') as fsrc, open(dst_file, 'wb') as fdst:
                while True:
                    # 读取数据块
                    buffer = fsrc.read(buffer_size)
                    if not buffer:
                        break

                    # 写入数据块到目的文件
                    fdst.write(buffer)

                    # 更新进度条
                    pbar.update(len(buffer))

        # 删除原文件
        os.remove(src_file)
        
    def move(self):
        if tsjCLI.checkFileExists(self.target_path):
            src_file = self.old_path + "\\" + self.filename
            dst_file = self.target_path + "\\" + self.filename
            # ic(src_file, dst_file)
            self.move_file_with_progress(src_file, dst_file)
        else:
            errorPrint("target_path not existed")