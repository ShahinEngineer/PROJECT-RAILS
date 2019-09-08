# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 21:10:59 2019

@author: Mohammad Shahin
"""
import sqlite3
from datetime import date
def create_connection(db_file):
    conn=None
    try:
        conn=sqlite3.connect(db_file)
    except Error as e:
        print(e)
        
    return conn

def create_track (conn,Name,AlbumId,MediaTypeId,GenreId,Composer,Milliseconds,Bytes,UnitPrice): 
    cursorObj = conn.cursor()
    cursorObj.execute("INSERT INTO tracks(Name,AlbumId,MediaTypeId,GenreId,Composer,Milliseconds,Bytes,UnitPrice) VALUES(?,?,?,?,?,?,?,?)",
                      (Name,AlbumId,MediaTypeId,GenreId,Composer,Milliseconds,Bytes,UnitPrice))
    conn.commit()

def get_tplaylist (conn):
    cursorObj = conn.cursor()
    #cursorObj.execute("SELECT * FROM playlists ", (track_id,))
    cursorObj.execute("SELECT * FROM playlists ")
    conn.commit()
    rows = cursorObj.fetchall()
    for row in rows:
        print(row,"\n")

def Create_paylist(conn):
    cursorObj = conn.cursor()
    cursorObj.execute('''CREATE TABLE IF NOT EXISTS Pylist2
         (paylist_id integer primary key AUTOINCREMENT,
          name varchar(255) NOT NULL)''')
    conn.commit()
    
def add_songs(conn,Name):
    cursorObj = conn.cursor()
    cursorObj.execute("INSERT INTO playlists (name) VALUES(?)",(Name,))

    conn.commit()

def Add_employy(conn,LastName,FirstName,Title,ReportsTo,BirthDate,HireDate,Address,City,State,Country,PostalCode,Phon,Faxe,Email):
    cursorObj = conn.cursor()
    cursorObj.execute("INSERT INTO employees(LastName,FirstName,Title,ReportsTo,BirthDate,HireDate,Address,City,State,Country,PostalCode,Phone,Fax,Email) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
                      (LastName,FirstName,Title,ReportsTo,BirthDate,HireDate,Address,City,State,Country,PostalCode,Phon,Faxe,Email,))
    conn.commit()
        
    

def delete_employees(conn, id):
    sql = 'DELETE FROM employees WHERE id=?'
    cur = conn.cursor()
    cur.execute(sql, (id,))
    conn.commit()

def add_purchase(conn,CustomerId,InvoiceDate,BillingAddres,BillingCitys,BillingState,
                 BillingCountry,BillingPostalCode,Total,TrackId,UnitPrice,Quantity):
    cursorObj = conn.cursor()
    cursorObj.execute("INSERT INTO invoices(CustomerId,InvoiceDate,BillingAddress,BillingCity,BillingState,BillingCountry,BillingPostalCode,Total) VALUES(?,?,?,?,?,?,?,?)",
                      (CustomerId,InvoiceDate,BillingAddres,BillingCitys,BillingState,BillingCountry,BillingPostalCode,Total))
    
    cursorObj.execute("INSERT INTO invoice_items(InvoiceId,TrackId,UnitPrice,Quantity) VALUES(?,?,?,?)",
                      (cursorObj.lastrowid,TrackId,UnitPrice,Quantity))
    #print(cursorObj.lastrowid)
    conn.commit()


conn= create_connection("C:/Users/Mohammad Shahin/Downloads/chinook.db")
while(True):
    value_input=input("plz select the option \n 1-Add Track  \n 2- Get a playlist \n 3- Create a playlist \n 4-Add a song t \n 5- Add an employee 6-Delete an employee \n 7-Report on a purchase \n 8-Print revenues \n 9-exsit \n")
    x=int(value_input)
    if x==9:
        break
    if x==1:
        name=input("Name \n")
        AlbumId=input("AlbumId as (Integer) \n")
        MediaTypeId=input("MediaTypeId as (Integer) \n")
        MediaTypeId=input("GenreId as (Integer) \n")
        GenreId=input("GenreId as (Integer) \n")
        Composer=input("Composer  \n")
        Bytes=input("Bytes as (Integer) \n")
        Milliseconds=input("Milliseconds as (Integer) \n")
        UnitPrice=input("Milliseconds as (Integer) \n")
        create_track(conn,name,int (AlbumId),int (MediaTypeId),int (GenreId),Composer,int(Bytes),int(Milliseconds),int(UnitPrice))
        print("Success")
        
    if x==2:
        get_tplaylist(conn)
        print("Success")
    if x==3:
        Create_paylist(conn)
        print("Success")
    if x==4:
        name=input("Song name \n")
        add_songs(conn,name)
        print("Success")
    if x==5:
        last=input("lastName \n")
        FirtName=input("FirtName  \n")
        Title=input("Title \n")
        ReportsTo=input("ReportsTo as (Integer) \n")
        
        BirthDate=input("BirthDate as (date) \n")
        HireDate=input("HireDate  as (date) \n")
        Address=input("Address  \n")
        City=input("City   \n")
        State=input("State \n")
        Country=input("Country \n")
        PostalCode=input("PostalCode \n")
        Phone=input("Phone \n")
        Fax=input("PostalCode \n")
        Email=input("Phone \n")
        
        Add_employy(conn,last,FirtName,Title,int (ReportsTo),date(BirthDate), date(HireDate),Address,City,State,Country,PostalCode,Phone,Fax,Email)
        print("Success")
    
    if x==6:
        id_emp=input("Employe as (Integer) \n")
        delete_employees(conn,id_emp)
        print("Success")
    if x==7:
        CustomerId =input("CustomerId  as (Integer) \n")
        InvoiceDate=input("InvoiceDate as (date)  \n")
        BillingAddress=input("BillingAddress \n")
        BillingCity=input("BillingCity \n")
        BillingState=input("BillingState \n")
        BillingCountry=input("BillingCountry \n")
        BillingPostalCode=input("BillingPostalCode \n")
        Total=input("Total \n")
        add_purchase(conn,int(CustomerId),date(InvoiceDate),BillingAddress,BillingCity,BillingState,BillingCountry,BillingPostalCode,int(Total))
        print("Success")
   
        
        
        
        
#create_track(conn,"Salim",22,95,1,"alaa",44,44,3)
#Create_paylist(conn)
#add_PlayList(conn,"Action")
#get_track(conn,1)
#Add_employy(conn,"mohammad","shahin","header", 12,date(2019, 4, 13), date(2019, 4, 13),"hebron","hebron","palestine","westbacnk","12","0598552131","1111","moabo.sha@hs.con")
#add_purchase(conn,2,date(2019, 4, 13),"hebron","hebron","hebron","palestine","123",22,2,22,24)

