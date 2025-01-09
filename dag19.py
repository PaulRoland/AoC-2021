# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
import itertools as it
start_time = time.time_ns()

def rotation(x1,y1,z1,x2,y2,z2):
    if x2==x1:    xr=[ 1, 0, 0]
    elif x2==y1:  xr=[ 0, 1, 0]
    elif x2==z1:  xr=[ 0, 0, 1]
    elif x2==-x1: xr=[-1, 0, 0]
    elif x2==-y1: xr=[ 0,-1, 0]
    elif x2==-z1: xr=[ 0, 0,-1]  

    
    if y2==x1:    yr=[ 1, 0, 0]
    elif y2==y1:  yr=[ 0, 1, 0]
    elif y2==z1:  yr=[ 0, 0, 1]
    elif y2==-x1: yr=[-1, 0, 0]
    elif y2==-y1: yr=[ 0,-1, 0]
    elif y2==-z1: yr=[ 0, 0,-1]    
    
    if z2==x1:    zr=[ 1, 0, 0]
    elif z2==y1:  zr=[ 0, 1, 0]
    elif z2==z1:  zr=[ 0, 0, 1]
    elif z2==-x1: zr=[-1, 0, 0]
    elif z2==-y1: zr=[ 0,-1, 0]
    elif z2==-z1: zr=[ 0, 0,-1]
    
    return [xr,yr,zr]

def translate(rot,x,y,z):
    nx=rot[0][0]*x+rot[1][0]*y+rot[2][0]*z
    ny=rot[0][1]*x+rot[1][1]*y+rot[2][1]*z
    nz=rot[0][2]*x+rot[1][2]*y+rot[2][2]*z
    return nx,ny,nz            
 
def move_translate(rot,x,y,z,dx,dy,dz):
    nx=rot[0][0]*x+rot[1][0]*y+rot[2][0]*z
    ny=rot[0][1]*x+rot[1][1]*y+rot[2][1]*z
    nz=rot[0][2]*x+rot[1][2]*y+rot[2][2]*z
    return dx+nx,dy+ny,dz+nz    
       


f = open("input.txt", "r")
scan_n=-1
scanners=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    if line=='':
        continue
    if '---' in line:
        scan_n+=1
        scanners.append([])
        continue
    
    scanners[scan_n].append([int(d) for d in line.split(',')])

    
f.close()


#Make a list of distances between each cubes.
#As istance is independent of coordinate system this can be used to find similarities
distances=dict()
for scan_n,scan in enumerate(scanners):
    for cube1,[x1,y1,z1] in enumerate(scan):
        lengths=list()
        for cube2,[x2,y2,z2] in enumerate(scan):
            if cube1==cube2:
                continue
            
            key1=str(scan_n)+'_'+str(cube1)+'_'+str(cube2)
            key2=str(scan_n)+'_'+str(cube2)+'_'+str(cube1)
            cur_dist=((x1-x2)**2+(y1-y2)**2+(z1-z2)**2)
            
            if cur_dist in distances:
                if key2 in distances[cur_dist]:
                    continue                  
                distances[cur_dist].append(key1)
            else:   
                distances.update({cur_dist:[key1]})

key_list=list()

#Remove distances with single scanner
for key in distances:
    if len(distances[key])<2:
        key_list.append(key)
for key in key_list:
    del distances[key]
    

scan_orientation=[[1,1,1] for scan in scanners]
scan_coords=[[0,0,0] for scan in scanners]
beacons=0
fixed_keys=[0]

while len(fixed_keys)<len(scanners):
    matches=dict()
    for key in distances:
        
        for key1,key2 in it.combinations(distances[key],2):
            n1,cube11,cube12=[int(d) for d in key1.split('_')]
            n2,cube21,cube22=[int(d) for d in key2.split('_')]
            
            if n1 not in fixed_keys and n2 not in fixed_keys:
                #Geen bekende referentie dus niet doorgaan
                continue
            elif n1 not in fixed_keys:
                #Als n1 een onbekende is swap n1 and n2
                    n1,cube11,cube12=[int(d) for d in key2.split('_')]
                    n2,cube21,cube22=[int(d) for d in key1.split('_')]
            if n2 in fixed_keys:
                continue
            
            #Find oringal distances in x,y,z for both scanners
            dx1 = (scanners[n1][cube11][0]-scanners[n1][cube12][0])
            dx2 = (scanners[n2][cube21][0]-scanners[n2][cube22][0])
            dy1 = (scanners[n1][cube11][1]-scanners[n1][cube12][1])
            dy2 = (scanners[n2][cube21][1]-scanners[n2][cube22][1])        
            dz1 = (scanners[n1][cube11][2]-scanners[n1][cube12][2])
            dz2 = (scanners[n2][cube21][2]-scanners[n2][cube22][2])
    
            #x1 should match in length with x2,y2 or z2
            if abs(dx1)==abs(dx2) or abs(dx1)==abs(dy2) or abs(dx1)==abs(dz2):
                #Determine rotation 
                rot = rotation(dx1,dy1,dz1,dx2,dy2,dz2)
                #Translate coordinates with rotation
                t_dx2,t_dy2,t_dz2=translate(rot,dx2,dy2,dz2)
    
                #Check if it is the exact same distance in x,y,z
                if dx1==t_dx2 and dy1==t_dy2 and dz1==t_dz2:

                    scan_x,scan_y,scan_z=translate(rot,scanners[n2][cube21][0],scanners[n2][cube21][1],scanners[n2][cube21][2])
                    
                    coords=[0,0,0]
                    coords[0]=scan_coords[n1][0]+scanners[n1][cube11][0]-scan_x
                    coords[1]=scan_coords[n1][1]+scanners[n1][cube11][1]-scan_y
                    coords[2]=scan_coords[n1][2]+scanners[n1][cube11][2]-scan_z

                    #Save both scanners and the translated location.
                    #Assume it has the same rotation if it has the same coordinate
                    dict_key = str(n1)+','+str(n2)+','+str(coords[0])+','+str(coords[1])+','+str(coords[2])
                    if dict_key in matches:
                        matches[dict_key][0]+=1
                    else:
                        matches.update({dict_key:[1,rot]})
    
    #Get best match, location and rotation
    match_list = list(matches.values())
    match_keys = list(matches.keys())
    best_match = match_keys[match_list.index(max(match_list))]
    bn1,bn2,bx,by,bz =[int(d) for d in best_match.split(',')]
    bx-=scan_coords[bn1][0]
    by-=scan_coords[bn1][1]
    bz-=scan_coords[bn1][2]
    brot=matches[best_match][1]
    #Change all data to same coordinate system as scanner 0
    for n,[x,y,z] in enumerate(scanners[bn2]):
        scanners[bn2][n]=move_translate(brot,x,y,z,bx,by,bz)
    fixed_keys.append(bn2)
    scan_coords[bn2]=(bx,by,bz)
    

total_cubes=set()
for scan in scanners:
    for cb in scan:
        key=','.join([str(s) for s in cb])
        total_cubes.add(key)
    
max_man_dist=0
for a,b in it.combinations(scan_coords,2):
    max_man_dist=max(max_man_dist,abs(a[0]-b[0])+abs(a[1]-b[1])+abs(a[2]-b[2]))
    
    

print("Part 1",len(total_cubes))
print("Part 2",max_man_dist)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))