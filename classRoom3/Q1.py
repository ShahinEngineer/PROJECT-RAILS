# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 21:58:47 2019

@author: Mohammad Shahin
"""
import random
##Question number 1
word="welcome"
string_wrods="welcome to my world"
dic_word="I love noodles and recursion"

number_between=[x for x in range(1,1000) if x%7==0]
number_have3=[x for x in range(1,1000) if '3' in str(x)]
remove_vowel="".join([char for char in word if char not in ("aeiou")])
find_word=[word for word in string_wrods.split(" ") if len(word)<4]
find_Beside1_9=set([number for number in range(1,1000) for divisor in [1,2,3,7] if number % divisor == 0])
dictionary_comprehension=lambda w:{word:len(word) for word in w.split(" ") }

#print(find_Beside1_9)

#Question number 2
def Add(number1,number2):
    return number1+number2

def Multiply(number1,number2):
    return number1*number2

def Modulo(number1,number2):
    return number1%number2

def Division(number1,number2):
    return number1/number2

def number(number1,number2):
    x=[Add(number1,number2),Multiply(number1,number2),Modulo(number1,number2),Division(number1,number2)]
    return(random.choice(x))
    
#print(number(10,5))

#Question three

def Fibonacci(number,st1):
    print(number,st1)
    if number-1==1 or number-2==1:
        return 1
    else:
        return (Fibonacci(number-1,"w")+Fibonacci(number-2,"ww"))


#print(Fibonacci(9,"mmm"))
        

#Quuestion  4
        
def getChange(s,n):
    if n==0:
        return 1
    if n<0:
        return 0
    
    if len(s)==0 and n>0:
        return 0
    
    return getChange(s[:-1],n)+getChange(s[:],n-s[-1])

    

#print(getChange([1,2,3],4))

def checkInMaterx(x,y,martrix):
    if x<0 or x>=len(martrix) or y<0 or  y>=len(martrix[0]):
        return False
    else:
        return True
    

def table(array,x,y,path=[]):
 
        
    if x==len(array)-1 and y==len(array)-1 and array[x][y]==0:
        return True
 
    if array[x][y]==0 :
        path.append((x,y))
        p1=False
        p2=False
        p3=False
        p4=False
        
        if(x-1,y) not in path and checkInMaterx(x-1,y,array):
            p1=table(array,x-1,y)
            if p1 ==True:
                path.append((x-1,y))
                
        if(x+1,y) not in path and checkInMaterx(x+1,y,array):
            p2=table(array,x+1,y)
            if p2 ==True:
                path.append((x+1,y))
        
        if(x,y-1) not in path and checkInMaterx(x,y-1,array):
            p3=table(array,x,y-1)
            if p3 ==True:
                path.append((x,y-1))
        
        if(x,y+1) not in path and checkInMaterx(x,y+1,array):
            p4=table(array,x,y+1)
            if p4 ==True:
                path.append((x,y+1))
        
        return p1 or p2 or p3 or p4
    
    else:
        return False
                
        

    

array=[[0,0,0,0],[0,0,0,0]]   

print(table(array,0,0,[]))
    

    
    
    
    
    
    


