
from math import *

        
def merge(intervals):
    intervals.sort()
    length=len(intervals)
    res=[]
    for i in range(length):
        if res==[]:
            res.append(intervals[i])
        else:
            size=len(res)
            if res[size-1][0]<=intervals[i][0]<=res[size-1][1]:
                res[size-1][1]=max(intervals[i][1], res[size-1][1])
            else:
                res.append(intervals[i])
    return res

def solve(N,P,cookies):
    base=sum(2*w+2*h for w,h in cookies)
    D=P-base
    intervals=sorted([[2*min(w,h),2*hypot(w,h)] for w,h in cookies])
    res=[]
    for l,r in intervals:
        if l>D: break
        res+=[[a+l,b+r] for a,b in res if a+l<=D]
        res+=[[l,r]]
        res=merge(res)
    if len(res)==0: return base
    last_l,last_r=res[-1]
    if D>last_r: return last_r+base
    return D+base 
     
     


cases=int(input())
for i in range(cases):
    N,P=tuple(map(int,input().split()))
    cookies=[tuple(map(int,input().split())) for _ in range(N)]

    print ("Case #%i: %.6f\n" %(i+1,solve(N,P,cookies)))