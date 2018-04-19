import sys
import math
import collections 
import heapq


def solve(B,M):
    if M>2**(B-2): return 'IMPOSSIBLE',[]
    grid=[['0']*(i+1)+['1']*(B-i-1) for i in range(B)]
    if M==2**(B-2): return 'POSSIBLE',[''.join(g) for g in grid]
    grid[0][B-1]='0'
    for i in range(B-2):
        if (M>>i)&1 ==0: 
        #ith digit represent connection from 1 to B-i-1 (0 to B-i-2) 
            grid[0][B-i-2]='0'
    return 'POSSIBLE',[''.join(g) for g in grid]


    


   


if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            B,M=tuple(map(int,next(in_f).split()))
            res,grid=solve(B,M)
            out_f.write("Case #%i: %s\n" %(i+1,res))
            if res=='POSSIBLE':
                for line in grid:
                    out_f.write(line+'\n')
             

