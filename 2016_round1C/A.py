import sys
import math
import collections 
import heapq


def solve(N,P):
    alpha='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total_p=sum(P)
    if N==2:
        return ' '.join(['AB']*P[0])
    ret=[]
    H=[(-p,alpha[i]) for i,p in enumerate(P)]
    heapq.heapify(H)
    while total_p>2:
        p,s=heapq.heappop(H)
        ret.append(s)
        p+=1 
        total_p-=1 
        if p<0: heapq.heappush(H,(p,s))
    ret.append(H[0][1]+H[1][1])
    return ' '.join(ret)



   


if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=int(next(in_f)[:-1])
            P=list(map(int,next(in_f).split()))
            out_f.write("Case #%i: %s\n" %(i+1,solve(N,P)))
             

