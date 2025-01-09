# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

f = open("input.txt", "r")

def print_image(pixels,nrow,ncol):
    print()
    count=0
    for cr in range(-55,nrow+55):
        s=''
        for cc in range(-55,ncol+55):
            if str(cr)+','+str(cc) in pixels:
                s+='\u2588'
                count+=1
            else:
                s+=' '
        print(s)
    print(count)
    


def enhance_image(pixels,nrow,ncol,offset):
    new_pixels=set()
    for cr in range(-6-offset,nrow+6+offset):
        for cc in range(-6-offset,ncol+6+offset):
            #find 9 bits
            enhance_bits=''
            for dr in[-1,0,1]:
                for dc in [-1,0,1]:
                    key=str(cr+dr)+','+str(cc+dc)
                    enhance_bits+=str(int(key in pixels))
                    
            enhance_int=int(enhance_bits,2)
            if enhance_key[enhance_int]=='1':
                new_pixels.add(str(cr)+','+str(cc))
    return new_pixels

enhance_key=f.readline().replace('#','1').replace('.','0').replace('\n','')
#enhance_key=[int(d) for d in f.readline().replace('#','1 ').replace('.','0 ').replace('\n','').split(' ')[:-1]]
f.readline()

pixels=set()
for row,line in enumerate(f):
    for col,s in enumerate(line):
        if s=='#':
            pixels.add(str(row)+','+str(col))
            
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
f.close()
nrow=row+1
ncol=col+1
#print_image(pixels,nrow,ncol)


for enhances in range(0,25):
    pixels=enhance_image(pixels,nrow,ncol,enhances*2)
    pixels=enhance_image(pixels,nrow,ncol,enhances*2+1)
    
    del_list=list()
    
    for pixel in pixels:
        cr,cc = [int(d) for d in pixel.split(',')]
        if cr>=-(enhances*2+2) and cr<nrow+(enhances*2+2) and cc>=-(enhances*2+2) and cc<ncol+(enhances*2+2):
            continue
        del_list.append(pixel)
    for pixel in del_list:
        pixels.remove(pixel)
    
    if enhances==0:
        total_p1=len(pixels)
    total_p2=len(pixels)
        

    #print_image(pixels,nrow,ncol)
    


print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))