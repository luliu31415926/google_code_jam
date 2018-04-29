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

def bfs(node,visited_,edge_dict):
    reachable=set()
    q=deque([node])
    while q:
        cur=q.popleft()
        reachable.add(cur)
        visited_[cur]=True 
        for neighbor in edge_dict[cur]:
            if not visited_[neighbor]: q.append(neighbor)
    return reachable


def check_feasible(v,stack,edge_dict,visited):
    # all nodes popped should be accesible to at least one of nodes left on stack
    if stack[-1]==v: return True 
    visited_=visited[:]
    reachable=set() 
    for i in range(len(stack)):
        if stack[i-1]==v:
            p=i 
            break 
        reachable.update(bfs(stack[i],visited_,edge_dict))
    for i in range(p,len(stack)):
        if stack[i] not in reachable: return False 
    while stack[-1]!=v:
        stack.pop()
    return True 



def solve(N,M,zips,flights):
    edge_dict=defaultdict(list)
    for u,v in flights:
        edge_dict[u-1].append(v-1)
        edge_dict[v-1].append(u-1)
    for key in edge_dict.keys():
        edge_dict[key].sort(key=lambda x: zips[x],reverse=True)
    start=min(list(range(N)),key=lambda x: zips[x])
    ret=''
    stack=[start]
    visited=[False]*(N)
    while stack:
        if stack[-1]==min(stack,key=lambda x:zips[x]):
            cur=stack.pop()
            if not visited[cur]:
                visited[cur]=True 
                ret+=zips[cur]  
                for neighbor in edge_dict[cur]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        else: 
            for v in sorted(stack,key=lambda x:zips[x]):
                if visited[v]: continue
                if check_feasible(v,stack,edge_dict,visited): 
                    break 
            cur=stack.pop()
            if not visited[cur]:
                visited[cur]=True 
                ret+=zips[cur]
                for neighbor in edge_dict[cur]:
                    if not visited[neighbor]:
                        stack.append(neighbor)

    return ret 




    

    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N,M=get_tuple(in_f)
            zips=[next(in_f)[:-1] for _ in range(N)]
            flights=[tuple(map(int,next(in_f).split())) for _ in range(M)]
            out_f.write("Case #%i: %s\n" %(i+1,solve(N,M,zips,flights)))
            

            
             

