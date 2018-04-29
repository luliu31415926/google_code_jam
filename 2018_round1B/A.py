
from math import *
from collections import *
from bisect import *


def solve(N,L,counts):
    A=[(c*10000//N)%100 for c in counts]+[0]*(N-L)
    A=[(50-c)%100 for c in A]
    K=(10000//N)%100 
    # use N-L K, to fill A to just over 50
    #if K==0: 

    Weight=[ceil(a/K) for a in A]
    Value=[50+a-w*K for a,w in zip(A,Weight)] 
    
    Cap=N-L
    dp=[0]*(Cap+1)
    for i in range(len(A)):
        for w in range(Cap,-1,-1):
            if Weight[i]<=w:
                dp[w]=max(dp[w-Weight[i]]+Value[i],dp[w])
    dp[Cap]




cases=int(input())
for i in range(cases):
    N,L=tuple(map(int,input().split()))
    counts=list(map(int,input().split()))

    print ("Case #%i: %i\n" %(i+1,solve(N,L,counts)))