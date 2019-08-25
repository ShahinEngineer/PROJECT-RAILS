# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:58:59 2019

@author: Mohammad Shahin
"""

print(0.1+0.2 ==3)
#Floating-point numbers are represented in computer hardware as base 2 (binary) fractions
#This is because you can not compare floating point value, as it cannot be considered precise. So the answer will come out as 0.3000000000004, 
#and python (and most languages) would consider that false.