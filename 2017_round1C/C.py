#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
import heapq

def calc(P,N,K):
	# probability of at least K of the N machine works 
	dp=[1]+[0]*K #dp[j] probability of at least j works 
	for p in P:
		for j in range(K,0,-1):
			dp[j]=dp[j-1]*p + dp[j]*(1-p)
	return dp[K]

def fill(P,i,U):
	#print (P,i,U)
	stack=P[:]
	cur=i
	while U>0 and cur>0:
		if (stack[cur-1]-stack[cur])*(i-cur+1)<=U:
			stack[cur:i+1]=[stack[cur-1]]*(i+1-cur)
			U-=(stack[cur-1]-stack[cur])*(i-cur+1)
			cur-=1 
		else:
			stack[cur:i+1]=[stack[cur]+U/(i+1-cur)]*(i+1-cur)
			U=0 
	if U>0:
		if U<=(1-stack[0])*(i+1):
			stack[:i+1]=[stack[0]+U/(i+1)]*(i+1)
			U=0
		else: 
			stack[:i+1]=[1]*(i+1)
			stack[i+1]+=(U-(1-stack[0])*(i+1))
	return stack 



def solve(N,K,U,P):
	P.sort(reverse=True) 
	U_copy=U
	i=-1
	while U>0:
		i+=1
		U-=(1-P[i])
	i-=1 
	U=U_copy 
	print ('start testing from',i )
	prob=fill(P,i,U)
	print ('filled probability',prob)
	cur_ret=calc(prob,N,K)
	print ('calculated result',cur_ret)
	while 1:
		i+=1
		prob=fill(P,i,U)
		ret=calc(prob,N,K)
		if cur_ret>=ret: break 
		cur_ret=ret
	return cur_ret
	

	

if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		cases=int(next(in_f)[:-1])
		for i in range(cases):
			N,K=tuple(map(int,next(in_f).split()))
			U=float(next(in_f)[:-1])
			P=list(map(float,next(in_f).split()))
			out_f.write("Case #%i: %f\n" %(i+1,solve(N,K,U,P)))
				
	        