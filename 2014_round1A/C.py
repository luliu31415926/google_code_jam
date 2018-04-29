import sys
from math import *
from heapq import *
from fractions import gcd
from collections import *
from sys import stderr
import bisect


def get_int(f):
    return int(next(f)[:-1])
def get_tuple(f):
    return tuple(map(int,next(in_f).split()))
def get_list(f):
    return list(map(int,next(in_f).split()))
def get_list_of_list(f,N):
    return [list(map(int,next(in_f).split())) for _ in range(N)]



def calc_prob(N):
    # calculate P(S|bad)
    # dp[j][i] probability of number j at position i 
    dp=[[0]*N for _ in range(N)]
    pmove=1/N
    pstay=1.0-1/N
    for i in range(N):
        dp[i][i]=1.0
    for k in range(N):
        print (k)
        for j in range(N):
            next_jk=sum(dp[j])*pmove
            for i in range(N):
                if i!=k:
                    dp[j][i]=dp[j][i]*pstay +dp[j][k]*pmove
            dp[j][k]=next_jk
    return dp
def solve(N,nums,dp):

    #P(good|S)=P(S|good)*0.5/(P(S|good)*0.5+P(S|bad)*0.5)
            # =1/N!/(1/N!+P(S/bad))
    # use naive bayes to assume independence 
    P=1.0
    for i,j in enumerate(nums):
        P*=dp[j][i]*N
    res=1/(1+P)
    print (res)
    if res>0.5: return 'GOOD'
    else: return 'BAD'

    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        dp=calc_prob(1000)
        for i in range(cases):
            N=get_int(in_f)
            nums=get_tuple(in_f)
            out_f.write("Case #%i: %s\n" %(i+1,solve(N,nums,dp)))
            

            
             

