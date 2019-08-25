# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:01:19 2019

@author: Mohammad Shahin
"""

import random
board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]
test_board=[[]]
fix_dic={}

def initialization():
    test_board=[[0 for i in range(9)] for j in range(9)]
        
    for i in range(30):
         x=random.randint(0,8)
         y=random.randint(0,8)
         value=random.randint(1,9)
         if valid(test_board,value,(x,y))==True and (x,y) not in fix_dic :
             fix_dic[(x,y)]=value
             test_board[x][y]=value
           
        

            
    return test_board
            
    
    
def slove(bord):
    find=find_empty(bord)
    print(find)
    if not find:
        return True
    else:
        row,col=find
    
    for i in range(1,10):
        if valid(bord,i,(row,col)) == True:
            bord[row][col]=i
            
            if slove(bord):
                return True
            bord[row][col]=0
        
    return False
            
    

def valid(bord,number,position):
    x=position[0]
    y=position[1]
    #checkRow=False, checkClo=False,checkRec=False
    #check colum
    for i in range(len(bord)):
        if bord[i][y] == number and position[0]!=i:
            return False
    #check row     
    for j in range(len(bord[0])):
        if bord[x][j] ==number and position[1]!=j:
            return False
    #checkBox
    box_x=x//3
    box_y=y//3
    
    for i in range(box_y*3,box_x*3+3):
        for j in range(box_x*3,box_y*3+3):
            if bord[i][j]==number and (i,j)!=position:
                return False
    
    return True 
    
    
     
    
    #print(x)
            
def print_board(bord):
    
    for i in range(len(bord)):
        if i%3==0 :
            print("- - - - - - - - - -  ")
        for j in range(len(bord[0])):
            if j %3 ==0 :
                print("|",end="")
            if j==8:
                print(bord[i][j])
            else:
                print(str(bord[i][j]) + " ", end="")
     
def find_empty(bord):
    for i in range(len(bord)):
        for j in range(len(bord[0])):
            if bord[i][j]==0:
                return (i,j)
    
    return None
            
#sloved_sudoku=slove(board)         
#print(sloved_sudoku)
print(initialization())
print_board(board)
slove(board)
print("___________________")
print_board(board)
