import sys
import math
import collections 
# bipartite matching 
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

def solve(N,topics):
    first={word:i for i,word in enumerate(list({f for f,_ in topics}))}
    second={word:i+len(first) for i,word in enumerate(list({s for _,s in topics}))}
    V=len(first)+len(second)
    graph=Graph(V)
    for f,s in topics:
        graph.add_edge(first[f],second[s])
    bmatch=graph.bipartite_matching()
    non_match=sum([1 for m in graph.match if m==-1])
    return N-bmatch-non_match



if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=int(next(in_f)[:-1])
            topics=[tuple(next(in_f).split()) for _ in range(N)]
            
            out_f.write("Case #%i: %i\n" %(i+1,solve(N,topics)))
             

