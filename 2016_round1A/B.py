import sys
import math
import collections 

def solve(lsts):
    counts=collections.defaultdict(int)
    for lst in lsts:
        for h in lst:
            counts[h]^=1 
    ret=[k for k,v in counts.items() if v&1]
    return ' '.join(map(str,sorted(ret)))

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=int(next(in_f)[:-1])
            lsts=[list(map(int,next(in_f).split())) for _ in range(2*N-1)]
            out_f.write("Case #%i: %s\n" %(i+1,solve(lsts)))
             

