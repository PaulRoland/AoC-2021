# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024
@author: Paul
"""

import time
start_time = time.time_ns()

mem =dict()
def insert_seq(string,depth):    
    memkey=string+','+str(depth)
    if memkey in mem:
        return mem[memkey]

    if depth==0:
        element_count=dict(elements)
        return element_count
    
    element_count=dict(elements)
    
    for (s1,s2) in zip(string,string[1:]):
        if s1+s2 in insertions:
            elems1 = insert_seq(s1+insertions[s1+s2],depth-1)
            elems2 = insert_seq(insertions[s1+s2]+s2,depth-1)
            element_count[insertions[s1+s2]]+=1
        else: 
            print("gebeurt dit ook? ")
    
        
        for key in elems1:
            element_count[key]+=elems1[key]+elems2[key]
        
    
    
    mem.update({memkey:element_count})
    return element_count




f = open("input.txt", "r")
seq=f.readline()[:-1]
f.readline()
insertions=dict()
elements=dict()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','').split(' ')
    insertions.update({line[0]:line[2]})
    elements.update({line[2]:0})
f.close()


elems_p1 = insert_seq(seq,10)
elems_p2 = insert_seq(seq,40)
for letter in seq:
    elems_p1[letter]+=1
    elems_p2[letter]+=1
values1=list(elems_p1.values())
values2=list(elems_p2.values())
values1.sort(reverse=True)
values2.sort(reverse=True)

print("Part 1",values1[0]-values1[-1])
print("Part 2",values2[0]-values2[-1])
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))