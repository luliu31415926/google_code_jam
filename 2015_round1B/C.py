import sys
from math import *
from heapq import *
from fractions import gcd
from collections import *
from sys import stderr
import bisect


def get_int(f):
    return int(next(f)[:-1])
def get_ints(f):
    return tuple(map(int,next(in_f).split()))
def get_list(f):
    return list(map(int,next(in_f).split()))
def get_ints_list(f,N):
    return [list(map(int,next(in_f).split())) for _ in range(N)]



eps=0.000001
def cnt_encounter(d,m,T):
    if T*360/m<720-d: return 0 
    return (T*360/m-(720-d))//360+1

def calc(T,hikers):
    total=[]
    for d,h,m in hikers:
        total+=[cnt_encounter(d,m+i,T) for i in range(h)]
    return sum(total)


def solve(N,hikers):
    # d,h,m 
    # min speed-time to catch each hiker
    catch=[]

    for d,h,m in hikers:
        catch+=[(m+i)*(360-d)/360 for i in range(h)]
    catch.sort(reverse=True)
    ret=len(catch)
    A=0 #number of hikers to catch
    T=float('inf')
    while A<len(catch):
        # 一点点提速 看哪个最小
        T=catch[A]+eps
        B=calc(T,hikers) #赶上来的人数
        ret=min(ret,A+B)
        if ret==0: return 0 
        A+=1 

    return ret 


    
    # 赶上+超过

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            N=get_int(in_f)
            hikers=get_ints_list(in_f,N)
            out_f.write("Case #%i: %i\n" %(i+1,solve(N,hikers)))
            

            
             

