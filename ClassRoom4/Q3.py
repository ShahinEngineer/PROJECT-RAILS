# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 20:53:05 2019

@author: Mohammad Shahin
"""

dic_invits={}
class Party(object):
    def __init__(self,party_name=''):
        self.party_name=party_name
        self.Friend_list={}
        self.Party_details=''
        
    def add_friend(self,Friend):
        self.Friend_list[Friend.getName()]=Friend.getName()
    def del_friend(self,Name):
        self.Friend_list.pop(Name,None)
    def send_invites(self,details):
        for i in self.Friend_list.keys():
            #dic_invits[i]=[details]
            dic_invits.setdefault(i, []).append(details)
            print(i)
            
class Friend(object):
    def __init__(self,name):
        self.name=name
    def getName(self):
        return self.name
    def setName(self,name):
        self.name=name
    def show_invite(self):
        return dic_invits[self.name][0]
        
party = Party("Midnight Pub")
party2 = Party("Midnight Pub2")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")

party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)

party2.add_friend(nick)
party2.send_invites("nigh club tomorrow welcome")
party.send_invites("Friday,...")
print(dic_invits)
print(nick.show_invite())



        
        
        
   