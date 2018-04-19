import sys
import math
import collections 


def solve(N,bffs):
    

    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=int(next(in_f)[:-1])
            bffs=list(map(int,next(in_f).split()))
            out_f.write("Case #%i: %i\n" %(i+1,solve(N,bffs)))
             

