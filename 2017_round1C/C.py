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


def solve_other(N,K,U,P):
	eps=0.0000001
	delta=0.0001
	print (U,delta)
	P.sort(reverse=True)
	if sum([1-p for p in P[:K]])<=U: return 1

	while U>eps:
		res=0
		max_i=-1
		for i in range(N):
			if P[i]+delta>1: continue
			P[i]+=delta
			temp=calc(P,N,K)
			if temp>res:
				res=temp
				max_i=i
			P[i]-=delta
		P[max_i]+=delta 
		U-=delta
	return calc(P,N,K)








def solve(N,K,U,P):
	eps=0.00000001
	P.sort(reverse=True)
	P=[1]+P 
	cur=K
	while U>eps and cur>0:
		#print (U,cur,P)
		if (P[cur-1]-P[cur])*(K+1-cur)<=U:
			U-=((P[cur-1]-P[cur])*(K+1-cur))
			P[cur:K+1]=[P[cur-1]]*(K+1-cur)
			cur-=1 
		else:
			P[cur:K+1]=[U/(K+1-cur)+P[cur]]*(K+1-cur)
			U=0 
	if U>eps: return 1
	return calc(P[1:],N,K)




	

	

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
				
	        