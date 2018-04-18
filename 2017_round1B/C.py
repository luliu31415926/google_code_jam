#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math

def warshall_floyd(dp,V):
	for k in range(V):
		for i in range(V):
			for j in range(V):
				if dp[i][k]+dp[k][j]<dp[i][j]:
					dp[i][j]=dp[i][k]+dp[k][j]

	return dp
def calc(N,horses,city_map):
	shortest_dist=[ [d if d!=-1 else float('inf') for d in row ] for row in city_map ]
	#print (shortest_dist)
	shortest_dist=warshall_floyd(shortest_dist,N)
	#print (shortest_dist)
	graph=[[float('inf')]*N for _ in range(N)]
	for i in range(N):
		horse_e,horse_s=horses[i]
		for j in range(N):
			if shortest_dist[i][j]<=horse_e:
				graph[i][j]=min(graph[i][j],shortest_dist[i][j]/horse_s)
	#print (graph)
	return warshall_floyd(graph,N)


def solve(N,Q,horses,city_map,queries):

	dist=calc(N,horses,city_map)
	return ' '.join(map(str,[dist[u-1][v-1] for u,v in queries]))

	
if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		N=int(next(in_f)[:-1])
		for i in range(N):
			N,Q=tuple(map(int,next(in_f).split()))
			horses=[tuple(map(int,next(in_f).split())) for _ in range(N)]
			city_map=[list(map(int,next(in_f).split())) for _ in range(N)]
			queries=[tuple(map(int,next(in_f).split())) for _ in range(Q)]
			out_f.write("Case #%i: %s\n" %(i+1,solve(N,Q,horses,city_map,queries)))
				
	        