# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()
import re
import itertools as it


def snail_add(data,line):
    return '['+data+','+line+']'


def magnitude(data):
    if len(data)==5:
        return 3*int(data[1])+2*int(data[3])
    else:
        data=data[1:-1]
        depth=0
        
        for j,s in enumerate(data):
            if s=='[':
                depth+=1
            elif s==']':
                depth-=1
            
            if depth==0:
                break
        print("Magnitude:",data)
        part_a=data[:j+1]
        part_b=data[j+2:]
        print(part_a,part_b)
        if len(part_a)>1 and len(part_b)>1:
            return 3*magnitude(data[:j+1]) + 2*magnitude(data[j+2:])
        elif len(part_a)>1:
            return 3*magnitude(data[:j+1]) + 2*int(part_b)
        else:
            return 3*int(part_a) + 2*magnitude(data[j+2:])

def process_snail(data):
    cont = True
    while cont:
        cont=False
        depth=0
        prev_depth=0
        for j,s in enumerate(data):
            if s=='[':
                depth+=1
            elif s==']':
                depth-=1
            #print(s,depth)
            if depth>=5 and depth!=prev_depth:
                cont=True
                #find first pair
                pair=re.search(r'\[\d+,\d+\]',data[j:])
                j=j+pair.start()
                
                prev_depth=depth
                num1 = re.search(r'\d+',data[j:])
                num2 = re.search(r'\d+',data[j+num1.end():])
                res_l=re.search(r'\d+',data[:j][::-1])
                res_haakje =re.search(r']',data[j:])
                res_r=re.search(r'\d+',data[j+res_haakje.start():])
                #print("Place 2 change:",data)
                #print("Place 2 change:",' '*j+'^')
                if res_l and res_r:
                    ind_1=j-res_l.end()
                    ind_2=j+res_haakje.start()+res_r.start()
                    data=data[:ind_1]+str(int(num1.group())+int(res_l.group()[::-1]))+data[j-res_l.start():j]+'0'+data[j+res_haakje.end():ind_2]+str(int(num2.group())+int(res_r.group()))+data[j+res_haakje.start()+res_r.end():]
                    #print("After explode: ",data)
                    #print('1',data.count('['),data.count(']'))
                    break
                elif res_l:
                    ind_1=j-res_l.end()
                    data=data[:ind_1]+str(int(num1.group())+int(res_l.group()[::-1]))+data[j-res_l.start():j]+'0'+data[j+res_haakje.end():]
                    #print("After explode: ",data)
                    #print('2',data.count('['),data.count(']'))

                    break
                elif res_r:
                    ind_2=j+res_haakje.start()+res_r.start()
                    data=data[:j]+'0'+data[j+res_haakje.end():ind_2]+str(int(num2.group())+int(res_r.group()))+data[j+res_haakje.start()+res_r.end():]
                    #print("After explode: ",data)
                    #print('3',data.count('['),data.count(']'))

                    break
        if cont==True:
            continue
        res_split = re.search(r'\d{2,}',data)
        if res_split:
            cont=True
            a=int(res_split.group())
            n1=int(a//2)
            n2=int(a-n1)
            data=data[:res_split.start()]+'['+str(n1)+','+str(n2)+']'+data[res_split.end():]
            #print("After split:   ",data)
            #print('4',data.count('['),data.count(']'))
    return data
    


f = open("input.txt", "r")
data=''

snailnumbers=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    snailnumbers.append(line)
    if i==0:
        data=line
        continue
    print(" ",data)
    print("+",line)
    data = snail_add(data,line)
    data = process_snail(data)
    print("=",data)
    print()
    
f.close()

#Bepaal magnitude
mag_p1 = magnitude(data)


max_mag=0
for a,b in it.combinations(snailnumbers,2):
    max_mag=max(max_mag,magnitude(process_snail(snail_add(a,b))))
    max_mag=max(max_mag,magnitude(process_snail(snail_add(b,a))))

print("Part 1",mag_p1)
print("Part 2",max_mag)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))


