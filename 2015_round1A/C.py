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

def calc(p,other):
    if len(other)==0: return 0
    other=[polar_angle(q[0]-p[0],q[1]-p[1]) for q in other]
    other+=[a+2*pi for a in other]
    other.sort()
    ret=float('inf')
    l,r=0,0
    while l<len(other) and other[l]<2*pi :
        l_boundary,r_boundary=other[l],other[l]+pi
        while other[l]-l_boundary<eps: l+=1 
        while r_boundary-other[r]>eps: r+=1 
        ret=min(ret,r-l) 
    return ret


def solve(N,points):
    # for each point, form lines with all other points, points to the left or to the right can be cut down and it will be on the edge 
    ret=[]
    for i in range(N):
        ret.append(calc(points[i],points[:i]+points[i+1:]))
    return ret
    



if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=get_int(in_f)
            points=get_ints_list(in_f,N)
            ret=solve(N,points)
            out_f.write("Case #%i:\n" %(i+1))
            for p in ret:
                out_f.write("%i\n"%p)

            
             

