import sys
import math

def solve(s):
    ret=s[0]
    for c in s[1:]:
        if c>=ret[0]:
            ret=c+ret 
        else:
            ret=ret+c 
    return ret 
    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        N=int(next(in_f)[:-1])
        for i in range(N):
            string=next(in_f)[:-1]
            out_f.write("Case #%i: %s\n" %(i+1,solve(string)))
             

