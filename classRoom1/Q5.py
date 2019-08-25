# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 20:13:38 2019

@author: Mohammad Shahin
"""



word=input("Choose whatever you like \n")
word_char=list(word)
print(word_char)
dic=[]
for i in word:
    dic.append('_')
lives=len(word)
correct=0
i=0
print(dic)
while(i<lives):
    y=input("Enter the character \n")
    if y in word_char:
        for x in word_char:
            if x==y:
                dic[word_char.index(y)]=y
                word_char[word_char.index(y)]=''
                correct+=1
        if correct ==len(word):
            break
    else:
        lives-=1
        
    
    print(' '.join(dic))

if correct ==len(word):
    print("you are win the word is \n",' '.join(dic))
else:
    print("you are loose")
    
    


        
    