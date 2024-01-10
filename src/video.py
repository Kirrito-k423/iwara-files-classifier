
from tsjPython.tsjCommonFunc import *
from tsjPython import gVal as glv
from tsjPython import tsjCLI 
import re

class Video():
    
    game2characters = {
        "原神":["神里凌华","雷电将军","甘雨","刻晴","优菈","八重神子"], 
        "崩坏三": [],
        "崩坏星穹铁道": [],
        
    }
    
    gameNickname = \
    {
        "原神":["Genshin"],    
    }
    
    characterNickname = {
        "雷电将军": ["Raiden Shogun", "雷电", "将军" , "雷電将軍"],
        "神里凌华": ["Ayaka"],
        "星铁鸭": [],
        "崩三大鸭": [],
        "心海":["kokomi"],
        "甘雨":[],
        "优菈":[],
        "八重神子":["八重","神子","Yae Miko","Miko"],
        "刻晴":[],
        
        # "":[""],
    }
    
    
    songName = [
        
    ]
    
    def __init__(self,path,filename):
        self.old_path = path
        self.filename = filename
        # set 
        [self.game, self.character, self.song] = ["","",""]
        self.regexInfo(filename)
        self.target_path = self.findTarget()
        if self.character:
            self.ready = "yes"
        else:
            self.ready = "no"
        
        
    def regexInfo(self,filename):
        # directly recognize game/charater/song name from filename
        for official_game, nicklist in self.gameNickname.items():
            # ic(official_game, nicklist)
            if re.search(official_game,filename):
                self.game=official_game
                ic("Match game {} : {} in {}".format(self.game, official_game, filename))
                break
            for nickname in nicklist:
                if re.search(nickname,filename):
                    self.game=official_game
                    ic("Match game {} : {} in {}".format(self.game, nickname, filename))
                    break
                
        for official_charater, nicklist in self.characterNickname.items():
            # ic(official_charater, nicklist)
            for nickname in nicklist:
                if re.search(nickname,filename):
                    self.character=official_charater
                    ic("Match character {} : {} in {}".format(self.character, nickname, filename))
                    break
            if self.character:
                break
            if re.search(official_charater,filename):
                self.character=official_charater
                ic("Match character {} : {} in {}".format(self.character, official_charater, filename))
                break
                
        for song in self.songName:
            if re.search(song,filename):
                self.song=song
                ic("Match song {} : {} in {}".format(self.song, song, filename))
                break
        
        # If no game name, find game name using the character name
        if not self.game:
            if self.character:
                for game, characterList in self.game2characters.items():
                    if self.character in characterList:
                        self.game = game
            
        
    def findTarget(self):
        # if gVal set , use it
        if self.character in glv._get("character2directory"):
            return glv._get("character2directory")[self.character]
        else:
            # or return base + game + charactor
            return glv._get("target_base_path")+"\\"+\
                    self.game+"\\"+\
                    self.character
        
    def print(self):
        if self.ready == "yes":
            passPrint(self.filename) 
        else:
            print(self.filename)
        if not self.game:
            errorPrint("game is empty")
        if not self.character:
            errorPrint("character is empty")
        if not tsjCLI.checkFileExists(self.target_path):
             errorPrint("target_path not existed")
        yellowPrint("Game \t\t{}\nCharacter \t{}\nSong \t{}".format(self.game, self.character, self.song))
        yellowPrint("Target path: \t{}".format(self.target_path))
        
    def move_file_with_progress(self, src_file, dst_file):
        import shutil
        from tqdm import tqdm
        import os
        # 获取文件大小
        file_size = os.path.getsize(src_file)

        # 设置每次读取的块大小
        buffer_size = 1024 * 1024  # 1MB

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
        src_file = self.old_path + "\\" + self.filename
        dst_file = self.target_path + "\\" + self.filename
        ic(src_file, dst_file)
        self.move_file_with_progress(src_file, dst_file)