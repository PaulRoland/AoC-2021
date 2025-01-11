# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re 
start_time = time.time_ns()

f = open("input.txt", "r")

def cubeon(volume):
    total_p1=0
    total_p2=0
    for stat,x1,x2,y1,y2,z1,z2 in volume:
        if stat==1:
            total_p2+=(x2-x1+1)*(y2-y1+1)*(z2-z1+1)
            
            if x1>=-50 and x1<=50 and y1>=-50 and y1<=50 and z1>=-50 and z1<=50:
                total_p1+=(min(x2,50)-x1+1)*(min(y2,50)-y1+1)*(min(z2,50)-z1+1)

    return total_p1,total_p2   
    

ranges=list()
min_x,min_y,min_z,max_x,max_y,max_z=0,0,0,0,0,0
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('\n','')
    [x1,x2,y1,y2,z1,z2]=[int(d) for d in re.findall('-?\d+',line)]
    
    if 'on' in line:
        status=1
    else:
        status=0
    
    ranges.append([status,x1,x2,y1,y2,z1,z2,i])
    
    min_x=min(min_x,x1)
    max_x=max(max_x,x2)
    min_y=min(min_y,y1)
    max_y=max(max_y,y2)
    min_z=min(min_z,z1)
    max_z=max(max_z,z2)
f.close()

volume=[[0,min_x,max_x,min_y,max_y,min_z,max_z]]
i=0
prev_iden=-1
while i<len(ranges):
    
    stat,x1,x2,y1,y2,z1,z2,iden=ranges[i]
    i+=1
    for vol_stat, vol_x1,vol_x2,vol_y1,vol_y2,vol_z1,vol_z2 in volume:
        if x1<vol_x1:
            continue
        if x1>=vol_x1 and x2<=vol_x2 and y1>=vol_y1 and y2<=vol_y2 and z1>=vol_z1 and z2<=vol_z2:
            #print("volume enclosed by one volume!")
            if stat==vol_stat:
                #print("was al goed, geen splitsingen noodzakelijk")
                break
            #split in 6 volumes + enclosed volume:
            #In een kubus liggen er 2 vlakken, 2 kolommen en 2 blokken rond een kubus in het midden

            #Vlakken links en rechts
            if vol_x1!=x1:
                volume.append([vol_stat,vol_x1,x1-1,vol_y1,vol_y2,vol_z1,vol_z2])
            if vol_x2!=x2:
                volume.append([vol_stat,x2+1,vol_x2,vol_y1,vol_y2,vol_z1,vol_z2])
            
            #kolommen achter/voor
            if vol_y1!=y1:
                volume.append([vol_stat,x1,x2,vol_y1,y1-1,vol_z1,vol_z2])
            if vol_y2!=y2:
                volume.append([vol_stat,x1,x2,y2+1,vol_y2,vol_z1,vol_z2])
            #blokken boven/onder
            if vol_z1!=z1:
                volume.append([vol_stat,x1,x2,y1,y2,vol_z1,z1-1])
            if vol_z2!=z2:
                volume.append([vol_stat,x1,x2,y1,y2,z2+1,vol_z2])
                
            volume.append([stat,x1,x2,y1,y2,z1,z2])
            #Remove old volume
            volume.remove([vol_stat,vol_x1,vol_x2,vol_y1,vol_y2,vol_z1,vol_z2])
            
            break
        
        elif x1>=vol_x1 and x1<=vol_x2 and y1>=vol_y1 and y1<=vol_y2 and z1>=vol_z1 and z1<=vol_z2:
            #print("volume is partly in this volume!")
            #print("split up volume!")
            #1 Stuk tot maximaal aan hoek van volume
            ranges.insert(i,[stat,x1,min(x2,vol_x2),y1,min(y2,vol_y2),z1,min(z2,vol_z2),iden])
            
            #2 Vlak dat uitsteekt
            if vol_x2<x2:
                ranges.insert(i,[stat,vol_x2+1,x2,y1,y2,z1,z2,iden])
            #3 balk bovenop
            if vol_z2<z2:
                ranges.insert(i,[stat,x1,min(x2,vol_x2),y1,y2,vol_z2+1,z2,iden])
            #4 balkje rechts van containing volume (y richting)
            if vol_y2<y2:
                ranges.insert(i,[stat,x1,min(x2,vol_x2),vol_y2+1,y2,z1,min(z2,vol_z2),iden])
            break
        

total_p1,total_p2=cubeon(volume)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))