import sys
from math import *
from heapq import *
from fractions import gcd
from collections import *
from sys import stderr


def get_int(f):
    return int(next(f)[:-1])
def get_ints(f):
    return tuple(map(int,next(in_f).split()))
def get_list(f):
    return list(map(int,next(in_f).split()))
def get_ints_list(f,N):
    return [list(map(int,next(in_f).split())) for _ in range(N)]



eps=0.000001
def calc(four,three, two, M,cnt):
    if M<=four:
        return cnt-4*M
    else:
        M-=four
        cnt-=4*four 
    if M<=three:
        return cnt-3*M
    else:
        M-=three
        cnt-=3*three
    if M<=two:
        return cnt-2*M
    else:
        return 0 


def solve(R,C,N):
    if N<=ceil(R*C/2): return 0 
    cnt=(R-1)*C+(C-1)*R
    M=R*C-N
    # special case when R<2 or C<2 
    if R==1 or C==1: 
        return cnt-2*M


    if (R*C)%2==0: # if one of them is even
        four=(R-2)*(C-2)//2 
        three=R+C-4
        two=2
        return calc(four,three,two,M,cnt)
    else:
        # try two cases 
        four1=(R-2)*(C-2)//2+1
        three1=R+C-6
        two1=4

        four2=(R-2)*(C-2)//2
        three2=R+C-2
        two2=0
        return min(calc(four1,three1,two1,M,cnt),calc(four2,three2,two2,M,cnt))




    


if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            R,C,N=get_ints(in_f)
            out_f.write("Case #%i: %i\n" %(i+1,solve(R,C,N)))
            

            
             

