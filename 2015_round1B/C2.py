import sys
from math import *
from heapq import *
from fractions import gcd
from collections import *
from sys import stderr
import bisect


def get_int(f):
    return int(next(f)[:-1])
def get_ints(f):
    return tuple(map(int,next(in_f).split()))
def get_list(f):
    return list(map(int,next(in_f).split()))
def get_ints_list(f,N):
    return [list(map(int,next(in_f).split())) for _ in range(N)]





def solve(N,hikers):
    catch=[]
    pass_me=[]
    for d,h,m in hikers:
        for i in range(h):
            heappush(catch,((360-d)*(m+i)/360,m+i)) #time, speed
    best=len(catch)
    cur=len(catch) 
    #while catch:
    while cur-len(catch)<best: # still have potential 
        if len(pass_me)==0 or pass_me[0][0]>catch[0][0]:
            t,m=heappop(catch)
            cur-=1
            best=min(best,cur)
        else:
            t,m=heappop(pass_me)
            cur+=1 
        heappush(pass_me,(t+m,m))
    return best 


    
    # 赶上+超过

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=get_int(in_f)
            hikers=get_ints_list(in_f,N)
            out_f.write("Case #%i: %i\n" %(i+1,solve(N,hikers)))
            

            
             

