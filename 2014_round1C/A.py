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


# 最小互质 
#relative primes 

def gcd(a,b):
    # O(logmax(a,b))
    if b==0: return a
    return gcd(b,a%b)
def rg(a,b):
    g = abs(gcd(a,b))
    assert g
    return a // g, b // g
def is_power_of_two(x):
    return x&(x-1)==0

def solve(P,Q):
    p,q=rg(P,Q)
    if not is_power_of_two(q): return 'impossible'

    ret=0
    while 1:
        p=2*p
        ret+=1 
        if p>=q: return ret 










    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            P,Q=tuple(map(int,next(in_f).split('/')))
            out_f.write("Case #%i: %s\n" %(i+1,solve(P,Q)))
            

            
             

