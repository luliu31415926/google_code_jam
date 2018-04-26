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


def calc_prob(target,keyboard,B):
    p=1.0
    K=len(keyboard)
    for t in target:
        p*=(B[t]/K)
    return p 

 


def calc_prefix(S):
    # find the longest length of the suffix that's also a prefix
    n=len(S)
    pi=[0]*n
    begin=1
    matched=0
    while (begin+matched<n):
        if S[begin+matched]==S[matched]:
            matched+=1 
            pi[begin+matched-1]=matched
        else:
            if matched==0: begin+=1
            else:
                begin+=matched-pi[matched-1]
                matched=pi[matched-1]
    return pi[-1] 

def max_possible(target,S):
    L=len(target)
    pre=calc_prefix(target)
    return 1+(S-L)//(L-pre)

def solve(K,L,S,keyboard,target):
    # linearity of expectation
    B=Counter(keyboard)
    if any(t not in B for t in set(target)): return 0
    ensure=max_possible(target,S)
    single_target=calc_prob(target,keyboard,B)
    return ensure-single_target*(S-L+1)



    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            K,L,S=get_ints(in_f)
            keyboard=next(in_f)[:-1]
            target=next(in_f)[:-1]
            out_f.write("Case #%i: %f\n" %(i+1,solve(K,L,S,keyboard,target)))
            

            
             

