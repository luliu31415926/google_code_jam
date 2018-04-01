#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import collections
import math
def ford_fulkerson(graph):
	# s -> t if s can destroy t if all other t is inactive 




	# return max_matchings edge pairs, left set of vertices, right set of vertices 

def get_available_actions(graph):


	# return subgraph where s->t if s can destroy t right now while all other t is active


def take_action(max_matchings,available_actions):
	# find overlapping between max_matchings and available actions
	# remove the s and t from both graths 
	# return actions taken 
def modify_M(max_matchings,useful_soldiers, target_turrets,available_actions):
	# for all s in max_matchings, if s has another connection to t' and t' not in max_matchings, make a switch 
	# return max_matchings


def solve(C,R,M,input_graph):
	# intialliy find a random max matching graph M (set of edge pairs)
	# define the set of soldiers as the target set 
	# find a graph G' from G where s->t if s can destroy t while all t is active 
	# while there are soldiers left in the set
	# 	modify M (for all s,t' in G': if s in G' and t' not in M, connect s to t' instead(wont affect others))
		# while there are overlap in M and G'
			# take action (remove s,t from G, s from target set )
			# regenerate G' 
	ret=[]
	
	max_matchings,useful_soldiers,target_turrets,=ford_fulkerson(graph)
	available_actions=get_available_actions(graph)
	while True:
		actions,max_matchings,available_actions=take_action(max_matchings,available_actions)
		if len(actions)==0: break 
		ret+=actions
		for s,t in actions:
			useful_soldiers.discard(s)
			target_turrets.discard(t)

	while len(useful_soldiers)>0:
		max_matchings=motify_M(max_matchings,useful_soldiers, target_turrets,available_actions)
		while True: 
			actions,max_matchings,available_actions=take_action(max_matchings,available_actions)
			if len(actions)==0: break 
			ret+=actions
			for s,t in actions:
				useful_soldiers.discard(s)

	return ret 
if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		cases=int(next(in_f)[:-1])
		for i in range(cases):
			C,R,M =tuple(map(int,next(in_f).split()))
			graph=[next(in_f)[:-1] for r in range(R)]
			max_turrets, actions=solve(C,R,M,graph)
			out_f.write("Case #%i: %i\n" %(i+1,max_turrets))
			for s,t in actions:
				out_f.write("%i %i\n" %(s,t))
			
		
	        