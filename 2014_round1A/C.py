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





def solve(C,D,V,old):
    old.sort()
    cur=1
    ret=0
    while cur<=V:
        if old and old[0]<=cur:
            cur=cur+C*old[0]
            old.pop(0)
        else:
            ret+=1 
            cur=cur+C*cur
    return ret

        
    



    


    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            C,D,V=get_ints(in_f)
            old=get_list(in_f)
            out_f.write("Case #%i: %i\n" %(i+1,solve(C,D,V,old)))
            

            
             

