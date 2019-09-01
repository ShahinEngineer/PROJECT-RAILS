# -*- coding: utf-8 -*-
"""
Created on Mon Aug 26 19:10:06 2019

@author: Mohammad Shahin
"""

class shape(object):
    
    def Area(self):
        return 0
        
    def perimter(self):
        return 0
        

class Square(shape):
    def __init__(self,length):
        self.__length=length
    def get_length(self):
        return self.length
    def set_length(self,length):
        self.__length=length
    
    def Area(self):
        return 0
    def perimter(self):
        return 0
        


class Circle(shape):
    def __init__(self,radius):
        self.radius=radius
    def get_length(self):
        return self.radius
    def set_length(self,radius):
        self.__length=radius
        
    def Area(self):
        return 0
    def perimter(self):
        return 0
        
    