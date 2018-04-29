
from math import *
from collections import *
from bisect import *


def calc(R,H,cake,h_cuts,r_count,single_row):
    
    if any(i*single_row not in r_count for i in range(1,H+2)): return False
    cur=0
    for i in range(1,H+1):
        cut=bisect_right(r_count,single_row*i)
        h_cuts.append((cur,cut-1))
        cur=cut 
    h_cuts.append((cur,R-1))
    return True 

def count(single_cell,h1,h2,c1,c2,cake):
    cnt=0
    for h in range(h1,h2+1):
        cnt+=cake[h][c1:c2+1].count('@')
    return cnt==single_cell

def solve(R,C,H,V,cake):
    r_count=[cake[0].count('@')]
    for i in range(1,R):
        r_count.append(cake[i].count('@')+r_count[i-1])
    total=r_count[-1]
    if total%((H+1)*(V+1))!=0: return 'IMPOSSIBLE'

    h_cuts=[]
    if not calc(R,H,cake,h_cuts,r_count,total//(H+1)): return 'IMPOSSIBLE'

    cake_col=list(map(list,zip(*cake)))
    c_count=[cake_col[0].count('@')]
    for i in range(1,C):
        c_count.append(cake_col[i].count('@')+c_count[i-1])
    c_cuts=[]
    if not calc(C,V,cake_col,c_cuts,c_count,total//(V+1)): return 'IMPOSSIBLE'
    single_cell=total//(H+1)//(V+1)
    for h1,h2 in h_cuts:
        for c1,c2 in c_cuts:
            if not count(single_cell,h1,h2,c1,c2,cake): return 'IMPOSSIBLE'
    return 'POSSIBLE'




cases=int(input())
for i in range(cases):
    R,C,H,V=tuple(map(int,input().split()))
    cake=[ list(input()) for _ in range(R)]

    print ("Case #%i: %s\n" %(i+1,solve(R,C,H,V, cake)))