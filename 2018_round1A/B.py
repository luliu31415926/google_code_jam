
from math import *
from collections import *
        
def calc(T,R,cashiers):
    finished=sorted([max(0,min((T-p)//s,m)) for m,s,p in cashiers],reverse=True)
    return sum(finished[:R])


def solve(R,B,C, cashiers):
    lb,ub=0,max(m*s+p for m,s,p in cashiers)+1 
    while ub-lb>1:
        mid=(ub+lb)//2
        if calc(mid,R,cashiers)>=B:
            ub=mid
        else: lb=mid 
    return ub 
    
    
     


cases=int(input())
for i in range(cases):
    R,B,C=tuple(map(int,input().split()))
    cashiers=[tuple(map(int,input().split())) for _ in range(C)]

    print ("Case #%i: %i\n" %(i+1,solve(R,B,C, cashiers)))