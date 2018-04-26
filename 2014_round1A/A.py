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



class Graph:
    def __init__(self,V):
        self.G=[[] for _ in range(V)]
        self.used=[False]*V
        self.match=[-1]*V
        self.V=V
    def add_edge(self,u,v):
        self.G[u].append(v)
        self.G[v].append(u)
    def dfs(self,v):
        self.used[v]=True
        for i in range(len(self.G[v])):
            u=self.G[v][i]
            w=self.match[u]
            if w<0 or (not self.used[w] and self.dfs(w)):
                self.match[v]=u
                self.match[u]=v
                return True
        return False
    def bipartite_matching(self):
        res=0
        for v in range(self.V):
            if self.match[v]<0:
                self.used=[False]*self.V
                if self.dfs(v):res+=1 
        return res 

def check(I,R,f):
    flipped=tuple(sorted([i^f for i in I]))
    return flipped==R


def match(I,R,L):
    flip=0
    bits=0
    for i in range(L):
        flip<<=1
        if I[i]!=R[i]:
            flip|=1 
            bits+=1
    return bits,flip



def solve(N,L,initial,required):
    flips=[]

    for i in range(N): 
        flips.append(match(initial[0],required[i],L))


    flips.sort()
    print (len(flips))
    I=[int(i,2) for i in initial]
    R=tuple(sorted([int(r,2) for r in required]))
    for bits,f in flips:
        if check(I,R,f): return str(bits)
    return 'NOT POSSIBLE' 


    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N,L=get_ints(in_f)
            initial=next(in_f).split()
            required=next(in_f).split()
            out_f.write("Case #%i: %s\n" %(i+1,solve(N,L,initial,required)))
            

            
             

