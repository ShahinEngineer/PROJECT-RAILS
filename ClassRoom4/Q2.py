# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 19:53:02 2019

@author: Mohammad Shahin
"""

class Text(object):
    def __init__(self,text='',font=''):
        self.text=text
        self.font=font
        
    def addText(self,text):
        self.text=self.text+text
    def getText(self):
        return self.text
    def setFont(self,font):
        self.font=font
    def getFont(self):
        return self.font
    def show(self):
        return '['+self.getFont()+']'+self.getText()+'['+self.getFont()+']'


class SaveText(object):
    numberVersion=0
    dic_version={}
    def save_text(self,Text):
        SaveText.dic_version[SaveText.numberVersion]={"Font":Text.getFont(),"Text":Text.getText()}
        SaveText.numberVersion+=1
    def get_version(self,number):
        return SaveText.dic_version[number]['Text']
        

text=Text()
saver=SaveText()
text.addText("there was nothing ")
text.setFont("Arial")
saver.save_text(text)
print(text.show())
print(saver.get_version(0))
        