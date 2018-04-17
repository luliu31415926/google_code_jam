import sys
import math
'''
sort each intervals by (s,e)
依次检查第一个interval
如果某个interval 不能跟其他的match， 比他们都小
那么之后的interval 更不可能跟它match, 可丢弃
如果一组interval match 了以后， 假设影响了后面的一组match:
后面的影响了的一组interval 至少有一个与其他都不想交（比它们都大或都小）
如比其他的都小， 那么这个ingredient现在的interval更不可能与他们相交
如比其他的都大， 那么其他的ingredient 现在的interval都不能与它相交
所以并不能多出一组match 
可match现在的这组interval 
'''
def check(intervals):
    smallest=None 
    smallest_e=float('inf')
    cur_l,cur_r=float('-inf'),float('inf')
    for i,(l,r) in enumerate(intervals):
        cur_l=max(cur_l,l)
        cur_r=min(cur_r,r)
        if r<smallest_e: 
            smallest=i 
            smallest_e=r
    if cur_r<cur_l: return smallest
    else: return -1 
def solve(N,P,R,Q):
    #print (N,P,R,Q)
    ranges=[[(math.ceil(q/1.1/R[i]),math.floor(q/0.9/R[i])) for q in Q[i]] for i in range(N)]
    ranges=[sorted(r) for r in ranges]
    cur=[0]*N
    cnt=0
    while max(cur)<P:
        #return -1 if can match, else return index of the smallest interval 
        ret=check([ranges[i][cur[i]] for i in range(N)])
        if ret==-1: 
            cur=[p+1 for p in cur]
            cnt+=1 
        else:
            cur[ret]+=1 
    return cnt

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        N=int(next(in_f)[:-1])
        for i in range(N):
            # N ingredients, P packages for each ingredients
            N,P=tuple(map(int,next(in_f).split()))
            R=list(map(int,next(in_f).split())) #one serving of ratatouille
            # Q[i][j]= quantity of ith ingredient's j'th package 
            Q=[list(map(int,next(in_f).split())) for _ in range(N)]
            out_f.write("Case #%i: %i\n" %(i+1,solve(N,P,R,Q)))
             

