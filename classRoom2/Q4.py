# -*- coding: utf-8 -*-
"""
Created on Thu Aug 22 01:09:41 2019

@author: Mohammad Shahin
"""

f=open("input.txt",'r')
line=f.readline()
dic={}
dic_material=[]
End=False
Report_dic={}
while line:
    if line.find("Day")!=-1:
        #print(line.find("Day"))
        key=line
        dic[line]=line
        dic_material=[]
        End=False
       
    elif End!=True:
        x=line[6:-1]
        y=line[0:6]
        #dic_material[line[6:-1]]=]
        #line=f.readline()
        #dic_material[x]=[y,line[0:6]]
        dic_material.append(y)
        dic_material.append(x)
        #dic_material.append(line[0:6])
        dic[key]=dic_material
        if line.find("End")!=-1:
            End=True
        #print(dic)
    #dic[k]={}
    line=f.readline()
    
f.close()
wirte_output=open('output.txt','w')
print(dic)
for item in dic:
    print(item)
    x=dic[item]
    wirte_output.write(item)
    for i in range(0,len(x)-2,2):
        print(x[i],x[i+2],x[i+1])
        output_str=x[i]+"-"+x[i+2]+" "+x[i+1]
        wirte_output.write(output_str)
        wirte_output.write('\n')
        time1=x[i]
        time2=x[i+2]
        if x[i+1] not in Report_dic:
            Report_dic[x[i+1]]=abs((abs(int(time2[0:2])-int(time1[0:2]))*60)-(abs(int(time2[-3:])-int(time1[-3:]))))
        else:
            Report_dic[x[i+1]]=abs(Report_dic[x[i+1]])+abs(((int(time2[0:2])-int(time1[0:2]))*60)- abs(int(time2[-3:])-int(time1[-3:])))
            
    
count=0
dic_pre={}
for pre in Report_dic:
    count+=Report_dic[pre]   

for value in Report_dic:
    dic_pre[value]=int((Report_dic[value]/count)*100)
    
wirte_output.write("\n")
wirte_output.write("Report \n")

for item_output in Report_dic:
    output_report=item_output+"\t"+str(Report_dic[item_output])+'\t'+str(dic_pre[item_output])+"%"
    wirte_output.write(output_report)
    wirte_output.write("\n")
    #print(item_output,Report_dic[item_output],dic_pre[item_output])
wirte_output.close()       
print(dic_pre)
print(Report_dic)
            
        
        



        
        
        
        