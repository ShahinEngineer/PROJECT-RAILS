# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 09:08:24 2019

@author: Mohammad Shahin
"""
dic_vowel ={'a':0,'e':0,'i':0,'o':0,'u':0,'A':0,'E':0,'I':0,'O':0,'U':0}
stringVowel="ZzYyXxVvTtSsRrQqPpNnMmLlKkBbCcDdFfGgHhJj!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"

import random
class human(object):
    def __init__(self,name):
        self.name=name
        self.text=''
    
    def sendMessage(self,text):
        self.text=text
        
    def getMessage(self):
        return self.text
    
    def getName(self):
        return self.name

    
class Robot(object):
    def __init__(self,serial_number):
        self.serial_number=serial_number
        
    def sendMessage(self,text):
        self.text=text
    def getMessage(self):
        return self.text
    
    def getName(self):
        return self.serial_number
        

class chat(object):
    def __init__(self):
        self.setHuman=None
        self.setRobot=None
    def connect_human(self,human):
        self.setHuman=human
    def connect_Robot(self,robot):
        self.setRobot=robot
    def show_human_dialogue(self):
        MessageText=''
        for char in  (self.setRobot.getMessage()):
            if char == '0':
                MessageText+=random.choice(list(dic_vowel.keys()))
            else:
                MessageText+=random.choice(stringVowel)
                
        print(self.setHuman.getName(),"said:",self.setHuman.getMessage())
        print(self.setRobot.getName(),"said:",MessageText)
    
    def show_robot_dialogue(self):
        MessageText=''
        for char in (self.setHuman.getMessage()):
            if char in dic_vowel :
                MessageText+'0'
            else:
                MessageText+='1'
                
        print(self.setHuman.getName(),"said:",MessageText)
        print(self.setRobot.getName(),"said:",self.setRobot.getMessage())
        


chat = chat()
karl = human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_Robot(bot)
karl.sendMessage("welcome")
bot.sendMessage('0011')

chat.show_human_dialogue()
chat.show_robot_dialogue()
    
    

    
    
        
    
        
        
        
        
        
        
        
        