# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def n_paths(start,end,visited,n_visits):
    n=0
    if start==end:
        return 1
            
    for opties in graph[start]:
        if opties=='start':
            continue

        new_visited=list(visited)
        new_visited.append(opties)
        if opties in small_caves and new_visited.count(opties)>n_visits:
            continue
        new_n_visits=n_visits
        if opties in small_caves and new_visited.count(opties)==n_visits and n_visits>1:
            new_n_visits=1  
        n+=n_paths(opties,end,new_visited,new_n_visits)
        
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

print("Part 1",n_paths('start','end',['start'],1))
print("Part 2",n_paths('start','end',['start'],2))
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))