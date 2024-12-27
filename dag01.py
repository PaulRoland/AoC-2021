# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")
numbers=[int(d) for d in f.readlines()]

p1=0
for a,b in zip(numbers,numbers[1:]):
    if b>a:
        p1+=1
p2=0
for a,b,c,d in zip(numbers,numbers[1:],numbers[2:],numbers[3:]):
    if b+c+d > a+b+c:
        p2+=1
                         
print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))