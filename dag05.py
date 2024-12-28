# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import re
start_time = time.time_ns()

def ranges(r1,r2,c1,c2):
    lijst_c = list(range(min(c1,c2),max(c1,c2)+1))
    lijst_r = list(range(min(r1,r2),max(r1,r2)+1))
    if c1>c2:
        lijst_c = lijst_c[::-1]
    if r1>r2:
        lijst_r = lijst_r[::-1]
    
    if len(lijst_c)>len(lijst_r):
        return [[lijst_r[0]]*len(lijst_c),lijst_c]
    if len(lijst_r)>len(lijst_c):
        return [lijst_r,[lijst_c[0]]*len(lijst_r)]
    return [lijst_r,lijst_c]
    
    

f = open("input.txt", "r")
visited=dict() #[hor/ver,diagonal]
for i,line in enumerate(f):
    [c1,r1,c2,r2]=[int(d) for d in re.findall(r'\d+',line)]
    [r_list,c_list]=ranges(r1,r2,c1,c2)
 
    if r1==r2 or c1==c2:
        #Fixed row or column
        for [r,c] in zip(r_list,c_list):
            key=str(r)+','+str(c)            
            if key in visited:
                visited[key][0]+=1
            else:
                visited.update({key:[1,0]})
    else:
        for [r,c] in zip(r_list,c_list):
            key=str(r)+','+str(c) 
            if key in visited:
                visited[key][1]+=1
            else:
                visited.update({key:[0,1]})
f.close()

p1=p2=0
for key in visited:
    if visited[key][0]>=2:
        p1+=1
    if visited[key][0]+visited[key][1]>=2:
        p2+=1

print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))