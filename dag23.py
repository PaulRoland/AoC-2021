# -*- coding: utf-8 -*-
"""
Created on Sat Nov 30 22:09:16 2024

@author: Paul
"""

import time
start_time = time.time_ns()


def makemove(data,cur_score,nstore):
    global best
    if cur_score>=best:
        return 9999999999
    
    
    keylist=list(data.keys())
    keylist.sort()
    memkey=''
    for keystuk in keylist:
        memkey+=keystuk+data[keystuk]
    
    if memkey in mem:
        return mem[memkey]
    
    #Kijk welke tekens niet goed staan
    if nstore==2:
        storage=[['',''] for _ in range(0,12)]
    elif nstore==4:
        storage=[['','','',''] for _ in range(0,12)]    
    move_letters=list()
    #print(data,cur_score)

    locs={'A':0,'B':1,'C':2,'D':3}         
    storage_col=[2,4,6,8]
    
    wrong_col=list()
    
    for key in data:
        r,c=[int(d) for d in key.split(',')]
        s=data[key]
        if r==0:
            move_letters.append([r,c,s])
        else:
            storage[c][nstore-r]=s
            
            if c!=storage_col[locs[s]]:
                if c in wrong_col:
                    continue
                #Laatste in deze storage zal moeten bewegen
                for row in range(1,nstore+1):
                    new_key=str(row)+','+str(c)
                    if new_key in data:
                        move_letters.append([row,c,data[new_key]])
                        wrong_col.append(c)
                        break
    #print(move_letters)
    
    
    moves=list()
    optimum=False
    
    for r,c,s in move_letters:
        if optimum==True:
            break
        for row in range(1,nstore+1):
            if storage_col[locs[s]] in wrong_col:
                break
            
            if storage[storage_col[locs[s]]][nstore-row]=='':
                path_open=True
                
                for cc in range(min(storage_col[locs[s]],c),max(storage_col[locs[s]],c)+1):
                    if r==0 and cc==c:
                        continue
                    if '0,'+str(cc) in data:
                        path_open=False
                        break
                if path_open==True:
                    moves.append([r,c,s,row,storage_col[locs[s]]])
                    optimum=True
                    #print("optimal path found")
                    break
                break

        if optimum==True:
            break
        
        #Bekijk andere opties
        if r==0:
            continue
        
        for tc in [0,1,3,5,7,9,10]:
            path_open=True
            for cc in range(min(tc,c),max(tc,c)+1):
                if cc==c:
                    continue
                if '0,'+str(cc) in data:
                    path_open=False
                    break
                
            if path_open==True:
                moves.append([r,c,s,0,tc])

    #print(moves)
    if len(move_letters)<1:
        best=min(cur_score,best)
        #print("Beste:",best)
        return best
    
    cost={'A':1,'B':10,'C':100,'D':1000}
    end_score=9999999999
    
    if optimum==True:
        new_data=dict(data)
        key1=str(moves[-1][0])+','+str(moves[-1][1])
        key2=str(moves[-1][3])+','+str(moves[-1][4])
        #print(key2)
        del new_data[key1]
        new_data.update({key2:moves[-1][2]})
        score=cost[moves[-1][2]]*(moves[-1][0]+moves[-1][3]+abs(moves[-1][1]-moves[-1][4]))

        #print(moves[-1])
        end_score=min(end_score,makemove(new_data,cur_score+score,nstore))
    else: #Er is geen perfecte move, branching
        for move in moves:
            new_data=dict(data)
            key1=str(move[0])+','+str(move[1])
            key2=str(move[3])+','+str(move[4])
            #print(key2)
            del new_data[key1]
            new_data.update({key2:move[2]})
            score=cost[move[2]]*(move[0]+move[3]+abs(move[1]-move[4]))
            end_score=min(end_score,makemove(new_data,cur_score+score,nstore))
    
    
    mem.update({memkey:end_score})
    return end_score
        


f = open("input.txt", "r")
start_locs=dict()
for row,line in enumerate(f):
    for col,s in enumerate(line):
        if s.isalpha():
            key=str(row-1)+','+str(col-1)
            start_locs.update({key:s})

f.close()
#print(start_locs)
best=20000
mem=dict()
makemove(start_locs,0,2)
print("Part 1",best)


f = open("input2.txt", "r")
start_locs=dict()
for row,line in enumerate(f):
    for col,s in enumerate(line):
        if s.isalpha():
            key=str(row-1)+','+str(col-1)
            start_locs.update({key:s})

f.close()
best=2000000000
mem=dict()
makemove(start_locs,0,4)
print("Part 2",best)

print("--- %s ms ---" % ((time.time_ns() - start_time)/1000000))