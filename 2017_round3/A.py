#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import collections
import math
import itertools
def solve(g):
	# dfs, count total number of nodes including root 
	cache=dict()


	def dfs(cur):
		# return the node count of subtree, including the root node
		# if ancestor == cur, do not count 
		if cur in cache: return cache[cur]
		if sum( int(c) for c in cur )>len(cur) or len(cur)==1: return 1 
		parent_sum=0
		parent_base=''
		for i,c in enumerate(cur):
			parent_base+=(int(c)*str(i+1))
			parent_sum+=(i+1)*int(c)
		if parent_sum>len(cur):
			#print (parent_sum)
			#compute cnt directly， calculate unique permutations 
			cnt=[int(c) for c in cur if c!='0']
			rest=len(cur)-sum(cnt)
			ret=math.factorial(len(cur))/math.factorial(rest)
			for c in cnt:
				ret/=math.factorial(c)
			cache[cur]=int(ret)+1
			#print (ret)
			return int(ret)+1

		parent_base+=('0'*(len(cur)-len(parent_base)))
		parents=list(set(itertools.permutations(parent_base)))
		cnt=1
		for p in parents:
			if p==cur: continue 
			if p in cache: continue 
			cnt+=dfs(p)
		cache[cur]=cnt
		#print (cur,parent_base,cnt)
		return cnt

	return dfs(tuple(g)) 

'''
when the sum of digits is larger than L, we no longer need to find its ancestors
simply cnt the unique permutations of its parents digits. 
https://en.wikipedia.org/wiki/Stars_and_bars_(combinatorics)
for L=9, all the unique permutations with sum less than 9= 10+9-1 choose 10 
explaination:
theorm 2 of stars and bars (allow empty bins) for sum=n and num=k, unique permutation = (n+k-1) choose n
for sum<=n, simply assign an extra bin to contain the leftovers, 
therefore unique permutations=(n+1+k-1) choose (n+1)
'''
	
if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		cases=int(next(in_f)[:-1]) 
		for i in range(cases):
			googlement=next(in_f)[:-1]
			out_f.write("Case #%i: %i\n" %(i+1,solve(googlement)))
			
		
	        