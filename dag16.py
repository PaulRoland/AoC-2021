# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def product(numbers):
    prod=1
    for val in numbers:
        prod*=val
    return prod

def read_packet(version,data,ind):
    V = int(data[ind:ind+3],2)
    T = int(data[ind+3:ind+6],2)
    
    version+=V
    ind+=6
    
    if T==4: #literal value
        bits=''
        while True:
            bits+=data[ind+1:ind+5]
            ind+=5
            if data[ind-5]=='0':
                return [version,int(bits,2),ind]

    #Operator
    I = data[ind]
    ind+=1
    if I=='0':
        #Volgende 15 bits zijn een getal die de lengte in bits aangeven
        total_bits=int(data[ind:ind+15],2)
        ind+=15
        
        org_index=ind
        values=list()
        while ind<org_index+total_bits:
            [version,value,ind]=read_packet(version,data,ind)
            values.append(value)
    else:
        #volgende 11 bits zijn een getal die de lengte in packets aangeven
        total_packets=int(data[ind:ind+11],2)
        ind+=11
        values=list()
        for _ in range(0,total_packets):
            [version,value,ind]=read_packet(version,data,ind)
            values.append(value)

            
    #Return afhankelijk van type operator
    if T==0: return [version,sum(values),ind]
    elif T==1: return [version,product(values),ind]
    elif T==2: return [version,min(values),ind]
    elif T==3: return [version,max(values),ind]
    elif T==5: return [version,int(values[0]>values[1]),ind]
    elif T==6: return [version,int(values[0]<values[1]),ind]        
    elif T==7: return [version,int(values[0]==values[1]),ind]
    
    
f = open("input.txt", "r")
data = f.readline().replace('\n','')
f.close()

#Convert Hex to Binary. Fix number of bits to 4*n
bit_data=bin(int(data,16))[2:].zfill(len(data)*4)
[total_p1,total_p2,_] = read_packet(0,bit_data,0)

print("Part 1",total_p1)
print("Part 2",total_p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))