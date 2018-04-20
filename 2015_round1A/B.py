import sys
import math
import collections 
import heapq
import functools


def get_int(f):
    return int(next(f)[:-1])
def get_ints(f):
    return tuple(map(int,next(in_f).split()))
def get_list(f):
    return list(map(int,next(in_f).split()))
def get_ints_list(f,N):
    return [list(map(int,next(in_f).split())) for _ in range(N)]
   
#最大公约数
def gcd(a,b):
    # O(logmax(a,b))
    if b==0: return a
    return gcd(b,a%b)
#最小公倍数 least common multiple
def lcm(a,b):
    return a*b//gcd(a,b)
def lcmm(args):
    ret=lcm(args[0],args[1])
    for num in args[2:]:
        ret=lcm(ret,num)
    return ret   
def calc(M):
    lcm=lcmm(M)
    #print (lcm)
    return sum(lcm//m for m in M)

def solve_small(B,N,M):
    if N<=B: return N
    Q=calc(M)
    N%=Q

    print (Q,N)
    if N==0:N=Q
    if N<=B: return N
    H=[(t,b) for b,t in enumerate(M)]# finish time,barber 
    heapq.heapify(H)
    N-=B
    while 1:
        # (N,H)
        finish_time,barber=heapq.heappop(H)
        N-=1 
        if N==0: return barber+1 
        heapq.heappush(H,(finish_time+M[barber],barber))




def count_served(T,M):
    return sum(math.ceil(T/m) for m in M)

def solve(B,N,M):
    # find the time when N-1 are served, and the next availabe barber is the answer
    lb,ub=0,max(M)*N+1
    while ub-lb>1:
        mid=(ub+lb)//2 
        s=count_served(mid,M)
        if s<N:
            lb=mid
        else:
            ub=mid
    # lb is right before N being picked up
    available=[b+1 for b,m in enumerate(M) if lb%m==0] 
    return available[N-count_served(lb,M)-1]
    



if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            B,N=get_ints(in_f)
            M=get_list(in_f)
            out_f.write("Case #%i: %i\n" %(i+1,solve(B,N,M)))
            
             

