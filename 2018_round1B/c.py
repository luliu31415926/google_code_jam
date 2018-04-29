
from math import *
from collections import *
from bisect import *


def solve(R,C,H,V,cake):
    




cases=int(input())
for i in range(cases):
    R,C,H,V=tuple(map(int,input().split()))
    cake=[ list(input()) for _ in range(R)]

    print ("Case #%i: %s\n" %(i+1,solve(R,C,H,V, cake)))