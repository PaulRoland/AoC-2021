# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


def check_bingo(card):
    for row in card:
        for num in row:
            found=True
            if num not in numbers_drawn:
                found=False
                break
        if found==True:
            return [True,row]
    for c in range(0,5):
        for r in range(0,5):
            found=True
            if card[r][c] not in numbers_drawn:
                found=False
                break
        if found==True:
            return [True,c]
    return [False,0]        
                
    

f = open("input.txt", "r")
numbers=[int(d) for d in f.readline().split(',')]
cardn=-1
cards=list()
for i,line in enumerate(f):
    if line=='\n':
        cards.append([])
        cardn+=1
        continue
    line=line.replace('(','').replace(')','').replace('=','').replace('\n','')
    cards[cardn].append([int(d) for d in line.split()])
    
    print(line)
    
f.close()
stop=False
numbers_drawn=list()

for number in numbers:
    numbers_drawn.append(number)
    for card in cards:
        [check,place]=check_bingo(card)
        if check==True:
            stop=True
            break
    if stop==True:
        break
number_called=number
card_set=set(card[0]+card[1]+card[2]+card[3]+card[4])
score_remainder=sum(list(card_set)) - sum(list(set(card[0]+card[1]+card[2]+card[3]+card[4]) & set(numbers_drawn)))
p1=score_remainder*number_called


numbers_drawn=list()
wins=list()
for number in numbers:
    numbers_drawn.append(number)
    for n,card in enumerate(cards):
        [check,place]=check_bingo(card)
        if check==True:
            wins.append(n)
        if len(set(wins))==len(cards):
            break
    if len(set(wins))==len(cards):
        break
number_called=number
card_set=set(card[0]+card[1]+card[2]+card[3]+card[4])
score_remainder=sum(list(card_set)) - sum(list(set(card[0]+card[1]+card[2]+card[3]+card[4]) & set(numbers_drawn)))
p2=score_remainder*number_called



print("Part 1",p1)
print("Part 2",p2)
print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))