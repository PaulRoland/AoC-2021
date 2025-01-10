# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import itertools as it
start_time = time.time_ns()

mem=dict()
def dirac_dice(s1,s2,p1,p2,level,depth):
    key=str(s1)+','+str(s2)+','+str(p1)+','+str(p2)
    if key in mem:
        return mem[key]
    
    wins1=0
    wins2=0
    
    for d1,d2,d3 in it.product([1,2,3],repeat=3):
        t1=d1+d2+d3
        np1=(p1+t1-1)%10+1
        ns1=s1+np1
        
        #Player 1 wins
        if ns1>=level:
            wins1+=1
            continue
        for d4,d5,d6 in it.product([1,2,3],repeat=3):
            t2=d4+d5+d6
            np2=(p2+t2-1)%10+1
            ns2=s2+np2
            
            #Player 2 wins
            if ns2>=level:
                wins2+=1
                continue
            
            #No winners > more branches
            [a,b]=dirac_dice(ns1,ns2,np1,np2,level,depth+1)
            wins1+=a
            wins2+=b
            
    mem.update({key:[wins1,wins2]})               
    return [wins1,wins2]
          
roll=0
start1=8
start2=6

pos1=start1
pos2=start2
score1=0
score2=0
while True:
    roll+=1
    steps=7-roll
    pos1=(pos1+steps-1)%10+1
    score1+=pos1
 
    if score1>=1000:
        total_p1=score2*roll*3
        break
    roll+=1
    steps=7-roll
    pos2=(pos2+steps-1)%10+1
    score2+=pos2
    if score2>=1000:
        total_p1=score1*roll*3
        break

[a,b]=dirac_dice(0,0,start1,start2,21,0)


print("Part 1",total_p1)
print("Part 2",max(a,b))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))