#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import collections
import math
def solve(F,edges):
	# solve for each connected component 
	# for each component obtain a spanning tree, assign a discovery time to each vertex 
	# assign all non_tree_edges = 1 following the root to leaf direction 
	# calculate the tree edge value from leaf to root inorder to balance each node to zero sum.
	# if tree edge ==0 or >F^2, then return impossible 
	edge_dict=collections.defaultdict(set)
	for u,v in edges:
		edge_dict[u].add((u,v))
		edge_dict[v].add((u,v))
	tree_edges=set()
	discovery_time=dict()
	edge_value_dict=dict()

	# dfs to assign discovery time, find spanning trees 
	# use iterative to avoid recursion depth exceeded error 
	stack=[]
	for v in range(1,F+1):
		if v not in discovery_time:
			# found a new connected component 
			stack.append((v,1,None))
			while stack:
				#print ('stack',stack)
				#print ('discovery_time',discovery_time)
				cur,time,tree_edge=stack.pop()
				if cur in discovery_time: continue 
				discovery_time[cur]=time
				if tree_edge is not None:
					tree_edges.add(tree_edge)
				for x,y in edge_dict[cur]:
					if x not in discovery_time:
						stack.append((x,time+1,(x,y)))
					elif y not in discovery_time:
						stack.append((y,time+1,(x,y)))


	#print ('tree_edges',tree_edges)
	# at this point, all vertex should have a discovery_time value, 
	# all tree_edges has been added to tree_edges set
	# assign all non_tree edges value 1 following root to leaf direction 
	for u,v in edges:
		if (u,v) not in tree_edges:
			edge_value_dict[u,v]=1 if discovery_time[u]<discovery_time[v] else -1
	#print (edge_value_dict)
	# from leaf to root, assign value to tree_edges 
	vertex=list(range(1,F+1))
	vertex.sort(key=lambda v: -discovery_time[v])
	#print (vertex)
	for v in vertex:
		if v not in edge_dict: continue #no edge connected to v.
		if discovery_time[v]==1: continue # root node does not need calculation 
		cnt=0
		tree_edge=None
		for x,y in edge_dict[v]:
			if (x,y) not in edge_value_dict: 
				tree_edge=(x,y)
				continue 
			else:
				if x==v: cnt-=edge_value_dict[x,y] # edge is going out 
				if y==v: cnt+=edge_value_dict[x,y] # edge is coming in 
		#print (v, tree_edge, cnt)
		if cnt==0 or abs(cnt)>F**2: return ['IMPOSSIBLE']
		edge_value_dict[tree_edge]=-cnt if discovery_time[tree_edge[0]]<discovery_time[tree_edge[1]] else cnt
	'''
	# check result is correct:
	for v in range(1,F+1):
		cnt=0
		for x,y in edge_dict[v]:
			if x==v:cnt-=edge_value_dict[x,y]
			if y==v: cnt+=edge_value_dict[x,y]
		if cnt!=0:
			print (F,edges)
			raise AssertionError()
	'''
	return [edge_value_dict[u,v] for u,v in edges]
			




	
if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		cases=int(next(in_f)[:-1])
		for i in range(cases):
			F,P =tuple(map(int,next(in_f).split()))
			edges=[tuple(map(int,next(in_f).split()))for j in range(P)]
			ret=solve(F,edges)
			out_f.write("Case #%i: %s\n" %(i+1,' '.join(list(map(str,ret)))))
			
		
	        