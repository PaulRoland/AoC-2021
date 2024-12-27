# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
counter=[0,0,0,0,0,0,0,0,0,0,0,0]
#counter=[0,0,0,0,0]
numbers=list()
#counter=[0,0,0,0,0]
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    for j,s in enumerate(line):
        if s=='0':
            counter[j]-=1
        else:
            counter[j]+=1
    numbers.append(line)
f.close()

gamma=''
epsilon=''
for s in counter:
    if s>0:
        gamma+='1'
        epsilon+='0'
    else:
        gamma+='0'
        epsilon+='1'

filtered=list(numbers)
for i in range(0,len(counter)):
    new_list=list()
    
    common='' 
    for num in filtered:

        common+=num[i]
    
    most_common='1'
    if common.count('0')>common.count('1'):
        most_common='0'
    for num in filtered:
        if num[i]==most_common:
            new_list.append(num)
    filtered=list(new_list)
    if len(filtered)==1:
        break
oxygen=filtered[0]

filtered=list(numbers)
for i in range(0,len(counter)):
    new_list=list()
    
    common='' 
    for num in filtered:
        common+=num[i]
    
    most_common='0'
    if common.count('0')>common.count('1'):
        most_common='1'
    for num in filtered:
        if num[i]==most_common:
            new_list.append(num)
    filtered=list(new_list)
    if len(filtered)==1:
        break
scrubber=filtered[0]

print("Part 1",int(gamma,2)*int(epsilon,2))
print("Part 2",int(oxygen,2)*int(scrubber,2))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))