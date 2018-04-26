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

def polar_angle(x,y):
    # 从正x轴到vector的角度in radian [0,2*pi) 
    return fmod(atan2(y,x)+2*pi,2*pi)

eps=0.000001
def calc(d):
    if d<=2: return 10*(d-1)
    cnt=calc(d-1)
    cnt+=int((ceil((d-1)/2)*'9'))+1
    cnt+=int(floor((d-1)/2)*'9')
    return cnt  

def solve(N):
    if N<=20: return N 
    # count number of digit of N 
    digit=len(str(N))
    cnt=calc(digit) # calculate for 1000000 
    if N==10**(digit-1): return cnt
    left_half=str(N)[:floor(digit/2)]
    right_half=str(N)[floor(digit/2):]
    if left_half=='1'+'0'*(floor(digit/2)-1):
        return cnt+N-10**(digit-1)
    if int(right_half)==0:
        return solve(N-1)+1
    else:
        reverse_left_half=int(left_half[::-1])
    cnt+=reverse_left_half
    cur=10**(digit-1)+reverse_left_half
    #make the flip
    cnt+=1 
    cur=int(str(cur)[::-1])
    cnt+=(N-cur)
    
    return cnt
    



if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=get_int(in_f)
            
            out_f.write("Case #%i: %i\n" %(i+1,solve(N)))
            

            
             

