import sys
import math
import collections 
import heapq



def get_int(f):
    return int(next(f)[:-1])
def get_ints(f):
    return tuple(map(int,next(in_f).split()))
def get_ints_list(f,N):
    return [list(map(int,next(in_f).split())) for _ in range(N)]
   

def solve(N,M):
    y=0
    x=0 #10s rate 
    for i in range(1,N):
        y+=max(0,M[i-1]-M[i])
        x=max(x,M[i-1]-M[i])
    z=0
    for i in range(1,N):
        z+=min(M[i-1],x)

    return y,z
    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=get_int(in_f)
            M=get_ints(in_f)
            y,z=solve(N,M)
            out_f.write("Case #%i: %i %i\n" %(i+1,y,z))
            
             

