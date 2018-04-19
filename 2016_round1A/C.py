import sys
import math
import collections 
class UF:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[0]*n
        self.cnt=n
    def find(self,x):
        p=self.parent[x]
        if p==x: return x
        else: self.parent[x]=self.find(p)
        return self.parent[x]
    def union(self,x,y):
        x=self.find(x)
        y=self.find(y)
        if x==y: return 
        if self.rank[x]<self.rank[y]:
            self.parent[x]=y
        else:
            self.parent[y]=x
            if self.rank[x]==self.rank[y]: self.rank[x]+=1 
        self.cnt-=1 
    def same(self,x,y):
        return self.find(x)==self.find(y)

def visit(i,uf,visited):
    visited[i]=True 
    for j in range(N):
        if i==j: continue 
        if uf.same(i,j):
            visited[j]=True

def find_cycle(i,bffs):
    discovery_time=[-1]*len(bffs)
    cur=i
    time=0
    discovery_time[i]=0
    while 1:
        if discovery_time[bffs[cur]-1]!=-1:
            #found circle 
            l=time-discovery_time[bffs[cur]-1]+1
            return l,cur,bffs[cur]-1
        else:
            time+=1
            cur=bffs[cur]-1
            discovery_time[cur]=time

def find_max_chain(node,incoming_dict,not_node):
    #print (node, incoming_dict)
    cur_level=incoming_dict[node][:]
    cur_level.remove(not_node)
    if len(cur_level)==0: return 0
    l=1 
    while 1:
        nxt_level=[]
        for n in cur_level:
            nxt_level+=incoming_dict[n]
        if len(nxt_level)>0:
            l+=1
            cur_level=nxt_level[:]
        else:
            break 
    return l 


def solve(N,bffs):
    #each connected component contain maximum one cycle 
    visited=[False]*N
    uf=UF(N)
    circles=[0]
    chains=[]
    incoming_dict=collections.defaultdict(list)

    for k,bff in enumerate(bffs):
        uf.union(k,bff-1)
        incoming_dict[bff-1].append(k)

    for i in range(N):
        if not visited[i]:
            l,n1,n2=find_cycle(i,bffs)
            #print (l,n1,n2)
            if l>2: circles.append(l)
            else: 
                chain_length=2+find_max_chain(n1,incoming_dict,n2)+find_max_chain(n2,incoming_dict,n1)
                chains.append(chain_length)
        visit(i,uf,visited)
    chain_sum=sum(chains)
    max_circle=max(circles)
    return max(chain_sum,max_circle)

    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=int(next(in_f)[:-1])
            bffs=list(map(int,next(in_f).split()))
            out_f.write("Case #%i: %i\n" %(i+1,solve(N,bffs)))
             

