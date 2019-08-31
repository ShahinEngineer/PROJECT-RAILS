# -*- coding: utf-8 -*-
"""
Created on Sat Aug 24 20:01:19 2019

@author: Mohammad Shahin
"""

import random
from copy import copy, deepcopy
board2 = [
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
board= [[5, 3, 0, 0, 7, 0, 0, 0, 0],
          [6, 0, 0, 1, 9, 5, 0, 0, 0],
          [0, 9, 8, 0, 0, 0, 0, 6, 0],
          [8, 0, 0, 0, 6, 0, 0, 0, 3],
          [4, 0, 0, 8, 0, 3, 0, 0, 3],
          [7, 0, 0, 0, 2, 0, 0, 0, 6],
          [0, 6, 0, 0, 0, 0, 2, 8, 0],
          [1, 0, 0, 4, 1, 9, 0, 0, 5],
          [0, 0, 0, 0, 9, 0, 0, 7, 9]]



grid=     [[0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0], 
          [0,0,0,0,0,0,0,0,0]]

test_board=[[]]
fix_dic={}
not_fix_dic={}
end_fix_dic={}
hit_dic={}
numbers=[1,2,3,4,5,6,7,8,9]


    
def initialization(grid,number_fix):
    count=0
    while count<number_fix:
        x=random.randint(0,8)
        y=random.randint(0,8)
        if (x,y) not in fix_dic :
            fix_dic[(x,y)]=grid[x][y]
            count+=1
        
    for i in range(len(grid)):
        hint_x=random.randint(i,len(grid)-1)
        hint_y=random.randint(0,len(grid[0])-1)
        for j in range(len(grid[0])):
            if (i,j) not in fix_dic:
                hit_dic[(hint_x,hint_y)]=grid[hint_x][hint_y]
                grid[i][j]=0
            



    #print(test_board)       
    return grid
            
    
    
def slove(grid):
    find=find_empty(grid)
    #print(find)
    if not find:
        return True
    else:
        row,col=find
    random.shuffle(numbers)
    for i in numbers:
        if valid(grid,i,(row,col)) == True:
            grid[row][col]=i
            
            if slove(grid):
                return True
            grid[row][col]=0
        
    return False
            
    
def valid(bo, num, pos):
    # Check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != i:
            return False

    # Check column
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] != i:
            return False

    # Check box
    box_x = pos[1] // 3
    box_y = pos[0] // 3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x * 3, box_x*3 + 3):
            if bo[i][j] == num and (i,j) != pos:
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
                if (i,j) in fix_dic:
                    print(".",bord[i][j])
                else:
                    print(bord[i][j])
                
            else:
                if (i,j) in fix_dic:
                     print("."+str(bord[i][j]) + " ", end="")
                else:
                    print(str(bord[i][j]) + " ", end="")
     
def find_empty(bord):
    for i in range(len(bord)):
        for j in range(len(bord[0])):
            if bord[i][j]==0:
                return (i,j)
    
    return None
def hit(grid,pos):
    print(grid[0][0])
    hit_array=[]
    valid_check_row=False
    valid_check_colm=False
    valid_check_box=False
    
    for num in range(1,10):
        for i in range(len(grid[0])):
            if grid[pos[0]][i] == num and pos[1] != i:
                valid_check_row=True
           
                
        # Check column
        for i in range(len(grid)):
            if grid[i][pos[1]] == num and pos[0] != i:
                valid_check_colm=True
            
        # Check box
        box_x = pos[1] // 3
        box_y = pos[0] // 3
    
        for i in range(box_y*3, box_y*3 + 3):
            for j in range(box_x * 3, box_x*3 + 3):
                if grid[i][j] == num and (i,j) != pos:
                    valid_check_box=True
        if valid_check_row ==False and valid_check_colm==False and valid_check_box==False:
            hit_array.append(num)
        valid_check_row=False
        valid_check_colm=False
        valid_check_box=False
        
            
        

    return hit_array
    
def main():         
    #sloved_sudoku=slove(board)         
    #print(sloved_sudoku)
    #test_board=initialization(12)
    #print_board(grid)
    #generate_solvedGrid()
    
    #print("___________________")
    #print_board(grid)
    while(True):
        slove(grid)
        saved_grid=deepcopy(grid) 
        print_board(saved_grid)
        number_fix_cell=input("Please enter the number of cells to fill [0-80]. \n")
        Live=80-int (number_fix_cell)
        print(len(grid)*len(grid[0]))
        if int(number_fix_cell)>80:
            print("Error: invalid number of cells to fill")
        else:
            test_board=initialization(grid,int(number_fix_cell))
            while(Live>0):
                print_board(test_board)
                user_input=input("plz enter x y z \n")
                x, y, z = user_input.split()
                if (int(x),int(y)) in fix_dic or (saved_grid[int(x)][int(y)]!=int(z) and int(z)!=0) :
                    print("Error: value is invalid")
                    if (int(x),int(y)) in hit_dic:
                        print(hit_dic[(int(x),int(y))])
                    Live-=1
                elif int(z) ==0 and (int(x),int(y)) not in fix_dic:
                    not_fix_dic[(int(x),int(y))]=int(z)
                    test_board[int(x)][int(y)]=int(z)
                else:
                    not_fix_dic[(int(x),int(y))]=int(z)
                    end_fix_dic[(int(x),int(y))]=int(z)
                    test_board[int(x)][int(y)]=int(z)
                    
                    #print_board(test_board)
                    #hit_array=hit(test_board,(int(x),int(y)))
                    #print("".join(hit_array))
                if len(end_fix_dic.keys())+len(fix_dic.keys())>=80:
                    break
                
        user_dec=input("do you want to restart/exit")
        if user_dec=="exit":
            break;
                    

if __name__ == '__main__':
    main()