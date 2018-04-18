#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
import heapq


def solve(Ac,Aj,Ac_lst,Aj_lst):
	lst=[]
	for s,e in Ac_lst:
		lst.append([s,e,0])
	for s,e in Aj_lst:
		lst.append([s,e,1])
	lst.sort() 
	c_inside_intervals=[] 
	j_inside_intervals=[]
	stack=[lst[0]]
	cnt=0
	for s,e,p in lst[1:]:
		if p!=stack[-1][-1] :
			# different person 
			cnt+=1 
			stack.append([s,e,p])
		else:
			# same person, collapse interval 
			pre_s,pre_e,pre_p=stack.pop()
			if p==0:
				c_inside_intervals.append(s-pre_e)
			if p==1:
				j_inside_intervals.append(s-pre_e)
			stack.append([pre_s,e,p])

	# check midnight switch 
	if stack[0][-1]==stack[-1][-1]:
		inside_interval=stack[0][0]+1440-stack[-1][1]
		if stack[0][-1]==0: c_inside_intervals.append(inside_interval)
		else: j_inside_intervals.append(inside_interval)
		stack[0][0]=0
		stack[-1][1]=1440 
	else: 
		cnt+=1 

	#print (stack,cnt)
	heapq._heapify_max(c_inside_intervals)
	heapq._heapify_max(j_inside_intervals)
	c_total,j_total=0,0
	for s,e,p in stack:
		if p==0: c_total+=(e-s)
		if p==1: j_total+=(e-s)
	while c_total>12*60:
		split_interval=heapq._heappop_max(c_inside_intervals)
		cnt+=2
		c_total-=split_interval
		#print ('splinting c interval',split_interval)
	while j_total>12*60:
		split_interval=heapq._heappop_max(j_inside_intervals)
		cnt+=2
		j_total-=split_interval
		#print ('splinting j interval',split_interval)

	return cnt 




	

if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		N=int(next(in_f)[:-1])
		for i in range(N):
			Ac,Aj=tuple(map(int,next(in_f).split()))
			Ac_lst=[tuple(map(int,next(in_f).split())) for _ in range(Ac)]
			Aj_lst=[tuple(map(int,next(in_f).split())) for _ in range(Aj)]
			out_f.write("Case #%i: %i\n" %(i+1,solve(Ac,Aj,Ac_lst,Aj_lst)))
				
	        