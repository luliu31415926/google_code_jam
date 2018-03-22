#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import collections
import math
import heapq
'''
for large dataset 
use coordinate compression

''' 
def solve(R,C,N,D,painted):
	# let the maximum value we can assign to each cell be the length of the path from a dummy node. 
	# the maximum bright value we can assign to each cell will be the shortest path from the dummy node
	# this condition is constrained by the N cells with fixed values 
	# if we can find a shorter path to the fixed cells, then its IMPOSSIBLE 
	# dijkstra has complexity O(VlogV) < bellman ford O(VE)
	DIRS=[(0,1),(1,0),(0,-1),(-1,0)]
	fixed_cells={(r,c):b for r,c,b in painted}
	decided_vertices={(-1,-1):0}
	candidates=[(b,r,c) for r,c,b in painted]
	heapq.heapify(candidates)
	cnt=0
	while candidates:
		cur_val,cur_r,cur_c=heapq.heappop(candidates)
		if (cur_r,cur_c) in decided_vertices: continue 
		if (cur_r,cur_c) in fixed_cells and cur_val<fixed_cells[cur_r,cur_c]:
			return 'IMPOSSIBLE'
		# add its undecided neighboring vertices
		for u,v in DIRS:
			new_r,new_c=cur_r+u,cur_c+v
			if 0<new_r<R+1 and 0<new_c<C+1 and (new_r,new_c) not in decided_vertices:
				heapq.heappush(candidates,(cur_val+D,new_r,new_c))
		decided_vertices[cur_r,cur_c]=cur_val
		cnt+=cur_val
		cnt%=(10**9+7)
		#print (decided_vertices)
	return cnt

	
if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		cases=int(next(in_f)[:-1])
		for i in range(cases):
			R,C,N,D=tuple(map(int,next(in_f).split()))
			painted=[tuple(map(int,next(in_f).split()))for j in range(N)]
			out_f.write("Case #%i: %s\n" %(i+1,solve(R,C,N,D,painted)))
			
	
	        