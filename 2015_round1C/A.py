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

def calc(x,y,W):
    #min guesses requrired to sink the ship 
    # x on the left, y on the right
    #x y <=W-1 
    res=int(log(x+y+2-W,2))
    if x==W-1: res+=W-1
    else:  res+=W-2 
    return res




def solve(R,C,W):
    res=R*(C//W)+W-1 
    if C%W!=0: res+=1 
    return res


    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            R,C,W=get_ints(in_f)
            out_f.write("Case #%i: %i\n" %(i+1,solve(R,C,W)))
            

            
             

