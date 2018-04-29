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

def group(s):
    ret=[]
    cnt=1
    p=1
    unique=s[0]
    while p<len(s):
        if s[p]!=s[p-1]:
            ret.append(cnt)
            cnt=1 
            unique+=s[p]
        else: 
            cnt+=1 
        p+=1 
    ret.append(cnt)
    return unique,ret 


def calc(row):
    # find median , calculate moves needed 
    row.sort()
    median=row[len(row)//2]
    return sum(abs(c-median) for c in row)

def solve(N,strings):
    base_string,base_group=group(strings[0])
    M=[[c] for c in base_group]
    for s in strings[1:]:
        unique,gp=group(s)
        if unique!=base_string : return 'Fegla Won'
        for i,c in enumerate(gp):
            M[i].append(c)
    return sum(calc(row) for row in M)



    

    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=get_int(in_f)
            strings=[next(in_f)[:-1] for _ in range(N)]
            out_f.write("Case #%i: %s\n" %(i+1,solve(N,strings)))
            

            
             

