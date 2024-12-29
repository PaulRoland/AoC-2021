# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
start_time = time.time_ns()

def draw_pixels(pixels):
    global r_max,c_max
    r = [-1-int(pixel[0]) for pixel in pixels]
    c = [int(pixel[1]) for pixel in pixels]
    
    factor=(max(c)-min(c))/(max(r)-min(r))
    
    plt.figure(figsize=(12,12/factor))
    ax=plt.gca()
    plt.axis('square')
    for cr,cc in zip(r,c):
        ax.add_patch(Rectangle((cc,cr),1,1))
    plt.axis([min(c),max(c)+1,min(r),max(r)+1])
    plt.show()
        
def unique_list(lijst_in):
    pixel_list=list()
    for pixel in lijst_in:
        pixel_list.append(str(pixel[0])+'_'+str(pixel[1]))
    pixel_list=list(set(pixel_list))
    lijst_uit=list()
    for px in pixel_list:
        pixel=[int(d) for d in px.split('_')]
        lijst_uit.append(pixel)
    return lijst_uit

def perform_fold(pixels,fold):
    folded=list()
    for pixel in pixels:
        if fold[0]=='y':
            if pixel[0]>fold[1]:
                folded.append([fold[1]+(fold[1]-pixel[0]),pixel[1]])
                continue
        elif fold[0]=='x':
            if pixel[1]>fold[1]:
                folded.append([pixel[0],fold[1]+(fold[1]-pixel[1])])
                continue
        folded.append(pixel)
    folded=unique_list(folded)
    return folded
     

f = open("input.txt", "r")
pixels=list()
folds=list()
r_max=0
c_max=0
for line in f:
    if line=='\n':
        break
    line=line.replace('(','').replace(')','').replace('\n','')
    [x,y]=[int(d) for d in line.split(',')]
    r_max=max(r_max,y)
    c_max=max(c_max,x)
    pixels.append([y,x])

for line in f:
    line=line.split(' ')[-1]
    [axis,n]=line.split('=')
    folds.append([axis,int(n)])   
f.close()


lengths=list()
for fold in folds:
    pixels=perform_fold(pixels,fold)
    lengths.append(len(pixels))
print("Part 1",lengths[0])
print("Part 2:")
draw_pixels(pixels)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))