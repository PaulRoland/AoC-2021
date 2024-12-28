# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""
def sortString(string):
    return ''.join(sorted(string))

import time
start_time = time.time_ns()

f = open("input.txt", "r")
data=list()
for i,line in enumerate(f):
    line=line.replace('| ','').replace('\n','')
    data.append(line.split(' '))
    
f.close()

len_dict={2:1,4:4,3:7,7:8}
count_dict={1:0,4:0,7:0,8:0}

for out in data:
    for i in range(10,14):
        if len(out[i]) in len_dict:
            count_dict[len_dict[len(out[i])]]+=1
            
total_p1=0
for key in count_dict:
    total_p1+=count_dict[key]


letters_org={'123567':0,'36':1,'13457':2,'13467':3,'2346':4,'12467':5,'124567':6,'136':7,'1234567':8,'123467':9}
###Part 2
total_p2=0
for dat in data:
    count_list={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    count_list_1478={'a':0,'b':0,'c':0,'d':0,'e':0,'f':0,'g':0}
    
    for n in dat[:10]:
        if(len(n)==3):
            len3=n
        if(len(n)==2):
            len2=n
        
        if len(n)==2 or len(n)==4 or len(n)==3 or len(n)==7:
            for let in n:
                count_list_1478[let]+=1
        for let in n:
            count_list[let]+=1
            
    new_letters=dict()
    new_letters.update({list(set(len3)-set(len2))[0]:'1'})
    
    for key in count_list:
        if count_list[key]==4:
            new_letters.update({key:'5'})            
        if count_list[key]==6: 
            new_letters.update({key:'2'})
        if count_list[key]==8 and key not in new_letters:
            new_letters.update({key:'3'})
        if count_list[key]==9:
            new_letters.update({key:'6'})
        if count_list[key]==7:
            if count_list_1478[key]==2:
                new_letters.update({key:'4'})
            if count_list_1478[key]==1:
                new_letters.update({key:'7'})
    
    digits=''
    for n in dat[10:]:
        string=n
        for key in new_letters:
            string=string.replace(key,new_letters[key])
        digits+=str(letters_org[sortString(string)])
    print(digits)
    total_p2+=int(digits)
        
print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))