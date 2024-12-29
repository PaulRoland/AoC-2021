# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


mem1=dict()
def n_paths(start,end,visited):
    visited.sort()
    key=start+','+','.join(visited)
    
    if key in mem1:
        return mem1[key]
    if start==end:
        return 1
    
    n=0        
    for opties in graph[start]:
        if opties=='start':
            continue

        new_visited=list(visited)
        if opties in small_caves and opties in visited:
            continue
        elif opties in small_caves:
            new_visited.append(opties)

        n+=n_paths(opties,end,new_visited)
    
    mem1.update({key:n})
    return n

mem2=dict()
def n_paths2(start,end,visited,double):
    visited.sort()
    key=start+'-'+','.join(visited)
    if key in mem2:
        return mem2[key]
    
    if start==end:
        return 1
    
    n=0        
    for optie in graph[start]:
        if optie=='start':
            continue

        new_visited=list(visited)
        new_double=double
        if optie in small_caves and optie in new_visited and double=='':
            #Een keer mogen we iets 2 keer bezoeken
            new_visited.append(optie)
            new_double=optie
        elif optie in small_caves and optie in new_visited: #Anders mogen we niet twee keer
            continue
        elif optie in small_caves:
            new_visited.append(optie)
            
        n+=n_paths2(optie,end,new_visited,new_double)
    
    mem2.update({key:n})
    return n

f = open("input.txt", "r")
graph=dict()
small_caves=dict()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    [key1,key2]=line.split('-')
    if key1 in graph:
        graph[key1].append(key2)
    else:
        graph.update({key1:[key2]})
    if key2 in graph:
        graph[key2].append(key1)
    else:
        graph.update({key2:[key1]})
    
    if key1.lower()==key1:
        small_caves.update({key1:0})
    if key2.lower()==key2:
        small_caves.update({key2:0})

f.close()

print("Part 1",n_paths('start','end',['start']))
print("Part 2",n_paths2('start','end',['start'],''))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))