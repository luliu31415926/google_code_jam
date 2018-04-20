import sys
import math
import collections 
import heapq


def solve_mark(J,P,S,K):
    res=J*P*min(S,K)
    grid=[]
    if K>=S:
        return res,[[j,p,s] for j in range(1,J+1) for p in range(1,P+1) for s in range(1,S+1)]
    cur=1
    for p in range(1,P+1):
        for j in range(1,J+1):
            for _ in range(K):
                grid.append([j,p,cur])
                cur+=1
                if cur>S:
                    cur=1
    return res, grid 
def getint():
    return int(stdin.readline())

def getints():
    return tuple(int(z) for z in stdin.readline().split())

def solve(j,p,s,k):
    if k >= p:
        return [(i1,i2,i3) for i1 in range(1,j+1) for i2 in range(1,p+1) for i3 in range(1,min(s,k)+1)]
    return [(i1,i2,(i1+i2+i3)%p) for i1 in range(1,j+1) for i2 in range(1,p+1) for i3 in range(1,k+1)]


    


   


if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            J,P,S,K=tuple(map(int,next(in_f).split()))
            grid=solve(J,P,S,K)
            out_f.write("Case #%i: %i\n" %(i+1,len(grid)))
            for line in grid:
                out_f.write(' '.join(map(str,line))+'\n')
             

