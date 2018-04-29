import sys
from math import *
from heapq import *
from fractions import gcd
from collections import *
from sys import stderr
import bisect


def get_int(f):
    return int(next(f)[:-1])
def get_tuple(f):
    return tuple(map(int,next(in_f).split()))
def get_list(f):
    return list(map(int,next(in_f).split()))
def get_list_of_list(f,N):
    return [list(map(int,next(in_f).split())) for _ in range(N)]



def solve(A,B,K):
    ret=0

    if K>2:
        safe_bits=int(log(K-1,2)) # (K-1) bits -1 
        if (A-1)<=(1<<safe_bits)-1 or (B-1)<=(1<<safe_bits)-1: return A*B 
        ret+= (B* (1<<safe_bits))
        ret+= (A-(1<<safe_bits))*(1<<safe_bits)
        for a in range(1<<safe_bits, A):
            for b in range(1<<safe_bits,B):
                #if int(log(a,2))>safe_bits and int(log(b,2))>safe_bits: break
                if a&b < K: ret+=1 
    else:
        for a in range(A):
            for b in range(B):
                #if a>0 and int(log(a,2))>0 and b>0 and  int(log(b,2))>0: break
                if a&b < K: ret+=1  
    return ret 

    

    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            A,B,K=get_tuple(in_f)
            out_f.write("Case #%i: %i\n" %(i+1,solve(A,B,K)))
            

            
             

