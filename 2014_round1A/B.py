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


def max_nodes(node,parent,edge_dict):
    # return size of biggest full binary tree, rooted at node 
    if parent==0 and len(edge_dict[node])<=1: return 1
    if parent!=0 and len(edge_dict[node])<=2: return 1 
    children=[max_nodes(child,node,edge_dict) for child in edge_dict[node] if child!=parent]
    children.sort()
    return children[-1]+children[-2]+1

def solve(N, edges):
    edge_dict=defaultdict(list)
    for u,v in edges:
        edge_dict[u].append(v)
        edge_dict[v].append(u)
    M=0
    for root in range(1,N+1):
        M=max(M,max_nodes(root,0,edge_dict))
    return N-M

    
        
    



    


    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=get_int(in_f)
            edges=[tuple(map(int,next(in_f).split())) for _ in range(N-1)]
            out_f.write("Case #%i: %i\n" %(i+1,solve(N,edges)))
            

            
             

