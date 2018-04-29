
from math import *
from collections import *
from bisect import *
def can_add(r,truth,pairs):
    # check if signs[r] flows one of the truth, if only one truth, add another truth 
    m,n=signs[r]
    if len(truth)==1: 
        m_,n_=truth[0]
        if m!=m_ and n!=n_:
            truth=[(m,n_),(m_,n)]
        return True 
    else:
        for m_,n_ in truth:
            if m==m_ or n==n_:
                return True 
        return False 

def update(l,truth,pairs)
    # remove the truth that accomodate signs[l]
    m,n=pairs[l]
    for key in truth.keys():
        

def solve(S,signs):
    pairs=[(d+a,d-b) for d,a,b in signs]
    l,r=0,1
    truth=[pairs[0]]
                        # truth: accommodate signs 
    max_len=1
    cnt=1
    while r<S:         
        if can_add(r,truth,pairs):
            if r-l+1>max_len:
                max_len=r-l+1
                cnt=1 
            elif r-l+1==max_len:
                cnt+=1 
            r+=1 
        else:
            l+=1 
            update(l,truth,pairs)
    return max_len,cnt





    




cases=int(input())
for i in range(cases):
    S=int(input())
    signs=[ tuple(map(int,input().split())) for _ in range(S)]

    print ("Case #%i: %s\n" %(i+1,solve(S,signs)))