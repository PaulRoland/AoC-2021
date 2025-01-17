# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()

def monad(instructions,number):
    wxyz=[0,0,0,0]
    ind={'w':0,'x':1,'y':2,'z':3}
    number_index=0
    
    for instr in instructions:
        
        if instr[0]=='inp':
            print(number_index,wxyz)
            if number_index>=len(number):
                return wxyz[3]
            wxyz[ind[instr[1]]]=int(str(number)[number_index])
            number_index+=1
            #print(str(number)[number_index-1])
            continue
        
        if instr[2] in ['w','x','y','z']:
            factor=int(wxyz[ind[instr[2]]])
        else:
            factor=int(instr[2])
        #print(factor)
        if instr[0]=='mul':
            wxyz[ind[instr[1]]]=wxyz[ind[instr[1]]]*factor
        elif instr[0]=='add':
            wxyz[ind[instr[1]]]=wxyz[ind[instr[1]]]+factor
        elif instr[0]=='div':
            wxyz[ind[instr[1]]]=wxyz[ind[instr[1]]]//factor
        elif instr[0]=='mod':
            wxyz[ind[instr[1]]]=wxyz[ind[instr[1]]]%factor
        elif instr[0]=='eql':
            wxyz[ind[instr[1]]]=int(wxyz[ind[instr[1]]]==factor)
    
    print(wxyz)
    return wxyz[3]

f = open("input.txt", "r")
instr=list()
for i,line in enumerate(f):
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    instr.append(line.split(' ')) 
f.close()

'''
inp w1
mul x 0		[w1, 0,0,0]
add x z		[w1, 0,0,0]
mod x 26	[w1, 0,0,0]
div z 1		[w1, 0,0,0]
add x 12	[w1,12,0,0]
eql x w		[w1, 0,0,0] #Kan nooit equal zijn
eql x 0		[w1, 1,0,0] #Altijd 1 want w1 kan niet 12 zijn
mul y 0		[w1, 1,0,0]
add y 25	[w1, 1,25,0]
mul y x		[w1, 1,25,0]
add y 1		[w1, 1,26,0]
mul z y		[w1, 1,26,0]
mul y 0		[w1, 1, 0,0]
add y w		[w1, 1,w1,0]
add y 6		[w1,1,w1+6,0]
mul y x		[w1,1,w1+6,0]
add z y		[w1,1,w1+6,w1+6]

inp w2		[w2,10,W1+6,(w1+6)]
mul x 0		[w2,0 ,w1+6,(w1+6)]
add x z		[w2,w1+6,w1+6,w1+6]
mod x 26	[w2,(w1+6)%26,w1+6,w1+6]
div z 1		[w2,(w1+6)%26,w1+6,w1+6]
add x 10	[w2,(w1+6)%26+10,w1+6,w1+6]
eql x w		[w2,(w1+6)%26+10,w1+6,w1+6] #Kan nooit equal zijn w1+6<26, w1+16 altijd > w2
eql x 0		[w2,1,w1+6,w1+6]
mul y 0		[w2,1,0,w1+6]
add y 25	[w2,1,25,w1+6]
mul y x		[w2,1,25,w1+6]
add y 1		[w2,1,26,w1+6]
mul z y		[w2,1,26,(w1+6)*26]
mul y 0		[w2,1,0,(w1+6)*26]
add y w		[w2,1,w2,(w1+6)*26]
add y 2		[w2,1,w2+2,(w1+6)*26]
mul y x		[w2,1,w2+2,(w1+6)*26]
add z y		[w2,1,w2+2,(w1+6)*26+(w2+2)]

inp w3		[w3,1,w2+2,(w1+6)*26+(w2+2)]
mul x 0		[w3,0,w2+2,(w1+6)*26+(w2+2)]
add x z		[w3,(w1+6)*26+(w2+2),w2+2,(w1+6)*26+(w2+2)]
mod x 26	[w3,((w1+6)*26+(w2+2))%26,w2+2,(w1+6)*26+(w2+2)]
div z 1		[w3,((w1+6)*26+(w2+2))%26,w2+2,(w1+6)*26+(w2+2)]
add x 10	[w3,((w1+6)*26+(w2+2))%26+10,w2+2,(w1+6)*26+(w2+2)]
eql x w		[w3,0,w2+2,(w1+6)*26+(w2+2)]	#((w1+6)*26+(w2+2))%26+10 kan nooit gelijk zijn aan w3 want >10
eql x 0		[w3,1,w2+2,(w1+6)*26+(w2+2)]
mul y 0		[w3,1,0,(w1+6)*26+(w2+2)]
add y 25	[w3,1,25,(w1+6)*26+(w2+2)]
mul y x		[w3,1,25,(w1+6)*26+(w2+2)]
add y 1		[w3,1,26,(w1+6)*26+(w2+2)]
mul z y		[w3,1,26,(w1+6)*26*26+(w2+2)*26]
mul y 0		[w3,1,0,(w1+6)*26*26+(w2+2)*26]
add y w		[w3,1,w3,(w1+6)*26*26+(w2+2)*26]
add y 13	[w3,1,w3+13,(w1+6)*26*26+(w2+2)*26]
mul y x		[w3,1,w3+13,(w1+6)*26*26+(w2+2)*26]
add z y		[w3,1,w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)]

inp w4		[w4,1,w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)]
mul x 0		[w4,0,w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)]
add x z		[w4,(w1+6)*26*26+(w2+2)*26+(w3+13),w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)]
mod x 26	[w4,((w1+6)*26*26+(w2+2)*26+(w3+13))%26,w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)]
div z 26	[w4,((w1+6)*26*26+(w2+2)*26+(w3+13))%26,w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
add x -6	[w4,(((w1+6)*26*26+(w2+2)*26+(w3+13))%26)-6,w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
eql x w		[w4,1,w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]	X= (W4 == (W3+13)-6)    		Geeft W4 = W3+7
eql x 0		[w4,0,w3+13,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
mul y 0		[w4,0,0,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
add y 25	[w4,0,25,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
mul y x		[w4,0,0,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
add y 1		[w4,0,1,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
mul z y		[w4,0,1,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
mul y 0		[w4,0,0,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
add y w		[w4,0,w4,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
add y 8		[w4,0,w4+8,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
mul y x		[w4,0,0,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
add z y		[w4,0,0,(w1+6)*26*26+(w2+2)*26+(w3+13)//26]
		[w4,0,0,(w1+6)*26+(w2+2)]


inp w5		[w5,0,0,(w1+6)*26+(w2+2)]
mul x 0		[w5,0,0,(w1+6)*26+(w2+2)]
add x z		[w5,(w1+6)*26+(w2+2),0,(w1+6)*26+(w2+2)]
mod x 26	[w5,((w1+6)*26+(w2+2))%26,0,(w1+6)*26+(w2+2)]
div z 1		[w5,((w1+6)*26+(w2+2))%26,0,(w1+6)*26+(w2+2)]
add x 11	[w5,((w1+6)*26+(w2+2))%26+11,0,(w1+6)*26+(w2+2)]
eql x w		[w5,0,0,(w1+6)*26+(w2+2)]				x Kan nooit gelijk zijn aan w5 +11 > w5
eql x 0		[w5,1,0,(w1+6)*26+(w2+2)]
mul y 0		[w5,1,0,(w1+6)*26+(w2+2)]
add y 25	[w5,1,25,(w1+6)*26+(w2+2)]
mul y x		[w5,1,25,(w1+6)*26+(w2+2)]
add y 1		[w5,1,26,(w1+6)*26+(w2+2)]
mul z y		[w5,1,26,(w1+6)*26*26+(w2+2)*26]
mul y 0		[w5,1,0,(w1+6)*26*26+(w2+2)*26]
add y w		[w5,1,w5,(w1+6)*26*26+(w2+2)*26]
add y 13	[w5,1,w5+13,(w1+6)*26*26+(w2+2)*26]
mul y x		[w5,1,w5+13,(w1+6)*26*26+(w2+2)*26]
add z y		[w5,1,w5+13,(w1+6)*26*26+(w2+2)*26+w5+13]

inp w6		[w6,1,w5+13,(w1+6)*26*26+(w2+2)*26+w5+13]
mul x 0		[w6,0,w5+13,(w1+6)*26*26+(w2+2)*26+w5+13]
add x z		[w6,(w1+6)*26*26+(w2+2)*26+w5+13,w5+13,(w1+6)*26*26+(w2+2)*26+w5+13]
mod x 26	[w6,w5+13,w5+13,(w1+6)*26*26+(w2+2)*26+w5+13]
div z 26	[w6,w5+13,w5+13,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
add x -12	[w6,w5+13-12,w5+13,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
eql x w		[w6,1,w5+13,((w1+6)*26*26+(w2+2)*26+w5+13)//26]		W6 = W5+13-12 = W5+1
eql x 0		[w6,0,w5+13,((w1+6)*26*26+(w2+2)*26+w5+13)//26]	
mul y 0		[w6,0,0,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
add y 25	[w6,0,25,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
mul y x		[w6,0,0,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
add y 1		[w6,0,1,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
mul z y		[w6,0,1,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
mul y 0		[w6,0,0,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
add y w		[w6,0,w6,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
add y 8		[w6,0,w6+8,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
mul y x		[w6,0,0,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
add z y		[w6,0,0,((w1+6)*26*26+(w2+2)*26+w5+13)//26]
		[w6,0,0,(w1+6)*26+(w2+2)]

inp w7		[w7,0,0,(w1+6)*26+(w2+2)]
mul x 0		[w7,0,0,(w1+6)*26+(w2+2)]
add x z		[w7,(w1+6)*26+(w2+2),0,(w1+6)*26+(w2+2)]
mod x 26	[w7,w2+2,0,(w1+6)*26+(w2+2)]
div z 1		[w7,w2+2,0,(w1+6)*26+(w2+2)]
add x 11	[w7,w2+2+11,0,(w1+6)*26+(w2+2)]
eql x w		[w7,0,0,(w1+6)*26+(w2+2)]				+13>w7 kan dus nooit
eql x 0		[w7,1,0,(w1+6)*26+(w2+2)]	
mul y 0		[w7,1,0,(w1+6)*26+(w2+2)]
add y 25	[w7,1,25,(w1+6)*26+(w2+2)]
mul y x		[w7,1,25,(w1+6)*26+(w2+2)]
add y 1		[w7,1,26,(w1+6)*26+(w2+2)]
mul z y		[w7,1,26,(w1+6)*26*26+(w2+2)*26]
mul y 0		[w7,1,0,(w1+6)*26*26+(w2+2)*26]
add y w		[w7,1,w7,(w1+6)*26*26+(w2+2)*26]
add y 3		[w7,1,w7+3,(w1+6)*26*26+(w2+2)*26]
mul y x		[w7,1,w7+3,(w1+6)*26*26+(w2+2)*26]
add z y		[w7,1,w7+3,(w1+6)*26*26+(w2+2)*26+w7+3]

inp w8
mul x 0		[w8,0,w7+3,(w1+6)*26*26+(w2+2)*26+w7+3]
add x z		[w8,(w1+6)*26*26+(w2+2)*26+w7+3,w7+3,(w1+6)*26*26+(w2+2)*26+w7+3]
mod x 26	[w8,w7+3,w7+3,(w1+6)*26*26+(w2+2)*26+w7+3]
div z 1		[w8,w7+3,w7+3,(w1+6)*26*26+(w2+2)*26+w7+3]
add x 12	[w8,w7+3+12,w7+3,(w1+6)*26*26+(w2+2)*26+w7+3]
eql x w		[w8,0,w7+3,(w1+6)*26*26+(w2+2)*26+w7+3]			w7+15 kan nooit w8 zijn
eql x 0		[w8,1,w7+3,(w1+6)*26*26+(w2+2)*26+w7+3]
mul y 0		[w8,1,0,(w1+6)*26*26+(w2+2)*26+w7+3]
add y 25	[w8,1,25,(w1+6)*26*26+(w2+2)*26+w7+3]
mul y x		[w8,1,25,(w1+6)*26*26+(w2+2)*26+w7+3]
add y 1		[w8,1,26,(w1+6)*26*26+(w2+2)*26+w7+3]
mul z y		[w8,1,26,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26]
mul y 0		[w8,1,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26]
add y w		[w8,1,w8,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26]
add y 11	[w8,1,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26]
mul y x		[w8,1,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26]
add z y		[w8,1,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]

inp w9		[w9,1,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
mul x 0		[w9,0,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
add x z		[w9,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
mod x 26	[w9,w8+11,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
div z 1		[w9,w8+11,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
add x 12	[w9,w8+23,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
eql x w		[w9,0,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]		w9 kan nooit w8+23 zijn
eql x 0		[w9,1,w8+11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
mul y 0		[w9,1,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
add y 25	[w9,1,25,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
mul y x		[w9,1,25,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
add y 1		[w9,1,26,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+w8+11]
mul z y		[w9,1,26,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26]
mul y 0		[w9,1,0,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26]
add y w		[w9,1,w9,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26]
add y 10	[w9,1,w9+10,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26]
mul y x		[w9,1,w9+10,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26]
add z y		[w9,1,w9+10,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26+w9+10]

inp w10		[w10,1,w9+10,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26+w9+10]
mul x 0		[w10,0,w9+10,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26+w9+10]
add x z		
mod x 26	[w10,w9+10,w9+10,(w1+6)*26*26*26*26+(w2+2)*26*26*26+(w7+3)*26*26+(w8+11)*26+w9+10]
div z 26	[w10,w9+10,w9+10,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
add x -2	[w10,w9+8,w9+10,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
eql x w		[w10,1,w9+10,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]		W10 = W9+8
eql x 0		[w10,0,w9+10,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
mul y 0		[w10,0,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
add y 25	[w10,0,25,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
mul y x		[w10,0,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
add y 1		[w10,0,1,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
mul z y		[w10,0,1,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
mul y 0		[w10,0,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
add y w		[w10,0,w10,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
add y 8		[w10,0,w10+8,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
mul y x		[w10,0,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
add z y		[w10,0,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]

inp w11		[w11,0,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
mul x 0		[w11,0,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
add x z		[w11,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11),0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
mod x 26	[w11,w8+11,0,(w1+6)*26*26*26+(w2+2)*26*26+(w7+3)*26+(w8+11)]
div z 26	[w11,w8+11,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]
add x -5	[w11,w8+11-5,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]
eql x w		[w11,1,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]			w8+11-5=w11 => W11=W8+6
eql x 0		[w11,0,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]	
mul y 0		[w11,0,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]	
add y 25	[w11,0,25,(w1+6)*26*26+(w2+2)*26+(w7+3)]	
mul y x		[w11,0,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]
add y 1		[w11,0,1,(w1+6)*26*26+(w2+2)*26+(w7+3)]
mul z y		[w11,0,1,(w1+6)*26*26+(w2+2)*26+(w7+3)]
mul y 0		[w11,0,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]
add y w		[w11,0,w11,(w1+6)*26*26+(w2+2)*26+(w7+3)]
add y 14	[w11,0,w11+14,(w1+6)*26*26+(w2+2)*26+(w7+3)]
mul y x		[w11,0,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]
add z y		[w11,0,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]

inp w12
mul x 0		[w12,0,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]
add x z		[w12,(w1+6)*26*26+(w2+2)*26+(w7+3),0,(w1+6)*26*26+(w2+2)*26+(w7+3)]
mod x 26	[w12,w7+3,0,(w1+6)*26*26+(w2+2)*26+(w7+3)]
div z 26	[w12,w7+3,0,(w1+6)*26+(w2+2)]
add x -4	[w12,w7+3-4,0,(w1+6)*26+(w2+2)]
eql x w		[w12,1,0,(w1+6)*26+(w2+2)]			W12=W7-1
eql x 0		[w12,0,0,(w1+6)*26+(w2+2)]	
mul y 0		[w12,0,0,(w1+6)*26+(w2+2)]
add y 25	[w12,0,25,(w1+6)*26+(w2+2)]
mul y x		[w12,0,0,(w1+6)*26+(w2+2)]
add y 1		[w12,0,1,(w1+6)*26+(w2+2)]
mul z y		[w12,0,1,(w1+6)*26+(w2+2)]
mul y 0		[w12,0,0,(w1+6)*26+(w2+2)]
add y w		[w12,0,w12,(w1+6)*26+(w2+2)]
add y 6		[w12,0,w12+6,(w1+6)*26+(w2+2)]
mul y x		[w12,0,0,(w1+6)*26+(w2+2)]
add z y		[w12,0,0,(w1+6)*26+(w2+2)]

inp w13		[w13,0,0,(w1+6)*26+(w2+2)]
mul x 0		[w13,0,0,(w1+6)*26+(w2+2)]
add x z		[w13,(w1+6)*26+(w2+2),0,(w1+6)*26+(w2+2)]
mod x 26	[w13,(w2+2),0,(w1+6)*26+(w2+2)]
div z 26	[w13,(w2+2),0,(w1+6)]
add x -4	[w13,w2-2,0,(w1+6)]
eql x w		[w13,1,0,(w1+6)]			W13=W2-2
eql x 0		[w13,0,0,(w1+6)]
mul y 0		[w13,0,0,(w1+6)]
add y 25	[w13,0,25,(w1+6)]
mul y x		[w13,0,0,(w1+6)]
add y 1		[w13,0,1,(w1+6)]
mul z y		[w13,0,1,(w1+6)]
mul y 0		[w13,0,0,(w1+6)]
add y w		[w13,0,w13,(w1+6)]
add y 8		[w13,0,w13+8,(w1+6)]
mul y x		[w13,0,0,(w1+6)]
add z y		[w13,0,0,(w1+6)]

inp w14
mul x 0		[w14,0,0,(w1+6)]
add x z		[w14,(w1+6),0,(w1+6)]
mod x 26	[w14,(w1+6),0,(w1+6)]
div z 26	[w14,(w1+6),0,0]
add x -12	[w14,(w1-6),0,0]
eql x w		[w14,1,0,0]				W14=W1-6
eql x 0		[w14,0,0,0]
mul y 0		[w14,0,0,0]
add y 25	[w14,0,25,0]
mul y x		[w14,0,0,0]
add y 1		[w14,0,1,0]
mul z y		[w14,0,1,0]
mul y 0		[w14,0,0,0]
add y w		[w14,0,w14,0]
add y 2		[w14,0,w14+2,0]
mul y x		[w14,0,0,0]
add z y		[w14,0,0,0]

Output altijd 0 als voldaan wordt aan:
W4=w3+7
W6=W5+1
W10=W9+8
W11=W8+6
W12=W7-1
W13=W2-2
W14=W1-6

Maximaal bij  01,02,03,04,05,06,07,08,09,10,11,12,13,14
W4=w3+7		     2, 9
W6=W5+1			   8, 9
W10=W9+8			       1, 9
W11=W8+6			    3,     , 9
W12=W7-1			 9,	      ,8
W13=W2-2	, 9                              , 7
W14=W1-6      9,                                    3
	     99298993199873

Minimaal bij  01,02,03,04,05,06,07,08,09,10,11,12,13,14
W4=w3+7		     1, 8
W6=W5+1			   1, 2
W10=W9+8			       1, 9
W11=W8+6			    1,     , 7
W12=W7-1			 2,	      ,1
W13=W2-2	, 3                              , 1
W14=W1-6      7,                                    1
	     73181221197111

   
'''
string='99298993199873'
scores = monad(instr,string)

string='73181221197111'
scores = monad(instr,string)



print("Part 1",'99298993199873')
print("Part 2",'73181221197111')
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))