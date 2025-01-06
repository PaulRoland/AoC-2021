# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

def trajectory(vx,vy,tx,ty):
    x=0
    y=0
    vy_i=vy
    while True:
        x+=vx
        y+=vy
        vy-=1
        
        if vx>0:
            vx-=1
        elif vx<0:
            vx+=1
        
        if y>=ty[0] and y<=ty[1]:
            if x>=tx[0] and x<=tx[1]:
                return [1,int(vy_i*(vy_i+1)/2)]
        elif y<ty[0]:
            return [0,0]


f = open("input.txt", "r")
max_height=0
for i,line in enumerate(f):
    [tx_l,tx_u,ty_l,ty_u]=[int(d) for d in re.findall(r'\d+',line)]
f.close()    

sol_list=list()
vx_option=list()
for vx in range(19,251):
    for vy in range(-105,105):
        [found,height] = trajectory(vx,vy,[tx_l,tx_u],[-ty_l,-ty_u])
        if found==1:
            sol_list.append([vx,vy,height])
            
        if height>max_height:
            max_height=max(height,max_height)

print("Part 1",max_height)
print("Part 2",len(sol_list))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))