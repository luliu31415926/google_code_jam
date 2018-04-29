
from math import *
from collections import *
        


def solve(N,P,cookies):
    base=sum(2*w+2*h for w,h in cookies)
    D=P-base
    I=sorted([[2*min(w,h),2*hypot(w,h)] for w,h in cookies])
    #dp[j] max right bound when l=j
    dp=defaultdict(int)
    for l,r in I:
        if l>D: break 
        for key in sorted(dp.keys()):
            if key+l>D: break 
            dp[key+l]=max(dp[key]+r,dp[key+l])
        dp[l]=max(dp[l],r)
    if len(dp)==0: return base 
    M=max(dp.values())
    if M>=D: return D+base
    else: return M+base

    
     


cases=int(input())
for i in range(cases):
    N,P=tuple(map(int,input().split()))
    cookies=[tuple(map(int,input().split())) for _ in range(N)]

    print ("Case #%i: %.6f\n" %(i+1,solve(N,P,cookies)))