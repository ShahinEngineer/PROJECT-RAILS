# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:00:25 2019

@author: Mohammad Shahin
"""
def interlaced(st1,st2):
    print(len(st2))
    small=''
    if len(st1)>len(st2):
        x=st1[len(st2):]
        small=st2[:]
    elif len(st2)>len(st1):
        x=st2[len(st1):]
        small=st1[:]
    res=''
    for i in range(len(small)):
        res+=st1[i]+st2[i]
    print(res+x)
    

interlaced("aaaa","bb")
