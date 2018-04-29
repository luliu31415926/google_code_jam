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

M=1000000007
def check(ret):
    s=''
    for sub,c in ret:
        s+=sub
    cnt=1
    for i in range(len(s)-1):
        if s[i]!=s[i+1]: cnt+=1 
    return cnt ==len(set(s))


def solve(N,strings):
    pure=defaultdict(int)
    start_with=dict()
    end_with=dict()
    left=set(strings)
    for s in strings:
        if len(set(s))==1: 
            pure[s[0]]+=1 
            if s in left:
                left.remove(s)
        else:
            if s[0] in start_with: return 0
            if s[-1] in end_with: return 0
            start_with[s[0]]=s
            end_with[s[-1]]=s
            
    #print (pure,start_with,end_with,left)
    ret=[]
    while left:
        cur=1
        s=left.pop()
        # deal with right side:
        while s[-1] in start_with or s[-1] in pure:
            if s[-1] in pure:
                cur*=factorial(pure[s[-1]])
                del pure[s[-1]]
            if s[-1] in start_with:
                tail=s[-1]
                if start_with[tail] in left:
                    left.remove(start_with[tail])
                s+=start_with[tail]
                del start_with[tail]
                

        # deal with left side:
        while s[0] in end_with or s[0] in pure:
            if s[0] in pure:
                cur*=factorial(pure[s[0]])
                del pure[s[0]]
            if s[0] in end_with:
                head=s[0]
                if end_with[head] in left:
                    left.remove(end_with[head])
                s=end_with[head]+s
                del end_with[head]
        ret.append((s,cur%M))
    for key,val in pure.items():
        ret.append((key,factorial(val)%M))
    #print (ret)
    if check(ret):
        product=1
        for _,c in ret:
            product*=c 
            product %=M 
        return product*factorial(len(ret))%M  
    else: return 0

    






    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=int(next(in_f)[:-1])
            strings=next(in_f).split()
            out_f.write("Case #%i: %s\n" %(i+1,solve(N,strings)))
            

            
             

