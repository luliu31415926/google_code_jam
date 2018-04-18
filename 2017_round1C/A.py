#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
import heapq

def calc(r,h):
	return 2*math.pi*r*h,math.pi*(r**2)
def check(i,pancakes,K):
	heap=[(*calc(rad,height),i) for i, (rad, height) in enumerate(pancakes)]
	heapq._heapify_max(heap)
	sides=[]
	while len(sides)<K-1:
		side,area,idx=heapq._heappop_max(heap)
		if idx==i: continue 
		sides.append(side)
	bottom_side,bottom_area=calc(*pancakes[i])
	return bottom_side+bottom_area+sum(sides)

def solve(N,K,pancakes):
	pancakes.sort(reverse=True)
	visited=set()
	ret=-1 
	for i,(r,h) in enumerate(pancakes):
		if r in visited: continue  # only check the same area with the most height
		ret=max(ret,check(i,pancakes,K))
		visited.add(r)
	return ret



	

if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		N=int(next(in_f)[:-1])
		for i in range(N):
			N,K=tuple(map(int,next(in_f).split()))
			pancakes=[tuple(map(int,next(in_f).split())) for _ in range(N)]
			out_f.write("Case #%i: %f\n" %(i+1,solve(N,K,pancakes)))
				
	        