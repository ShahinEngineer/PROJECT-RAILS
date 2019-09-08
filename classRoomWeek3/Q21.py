# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 00:09:03 2019

@author: Mohammad Shahin
"""

import sqlite3

def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
        
    return conn

def create_project(conn,name,subject,grade): 
    cursorObj = conn.cursor()
    cursorObj.execute("INSERT INTO students (name,subject,grade) VALUES(?,?,?)",(name,subject,grade))
    conn.commit()
        
    
    
 


conn= create_connection("C:/Users/Mohammad Shahin/Downloads/offi2.sqlite")
create_project(conn,"Salim","Math","95")
create_project(conn,"noor","history","94")
create_project(conn,"noor","Biology","96")
create_project(conn,"Salah","Math","80")
create_project(conn,"Salim","History","67")
create_project(conn,"Maria","Biology","73")
create_project(conn,"Noor","Math","100")
create_project(conn,"Maria","Math","100")
create_project(conn,"Maria","Math","50")
create_project(conn,"Salah","History","98")
create_project(conn,"Salim","Biology","85")


