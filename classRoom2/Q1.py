# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:38:18 2019

@author: Mohammad Shahin
"""

def count(st1):
    dic={}
    for i in st1:
        if i not in dic:
            dic[i]=1
        else:
            dic[i]+=1
        
    return dic

def Takelist(array):
    lista=[]
    for i in array:
        if type(i)==list:
            lista= lista+Takelist(i)
        else:
            lista.append(i)
    
    return lista
            

def url(str1):
    print(str1)
    dic={}
    schema=''
    for i in range(len(str1)):
        if str1[i] =='/' and str1[i+1]=='/':
            schema=str1[0:i-1]
            dic['schema']=schema
        if str1[i] =='.':
            dic['netloc']=str1[i+1:i+4]
            dic["path"]=str1[i+5:]
            break
        
    return(dic)
        
        
        
        
        
#print(count("welcomewww"))
print(Takelist([1,2,[3,[4,5],6,7,[8,9]],4]))
#print(url("https://google.com/project/Rails/kiss"))
        