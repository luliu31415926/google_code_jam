#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math

def calc(N,R,Y,B):
	colors=[(R,'R'),(Y,'Y'),(B,'B')]
	colors.sort()
	if colors[-1][0]>N//2: return None 
	string=['#']*N
	cur_cnt,cur_color=colors.pop()
	cur_idx=0
	for i in range(cur_cnt):
		string[i*2]=cur_color
	cur_idx=2*cur_cnt
	cur_cnt,cur_color=colors.pop()
	while cur_idx<N:
		cur_cnt-=1 
		string[cur_idx]=cur_color 
		cur_idx+=2 
	cur_idx=1
	while cur_cnt>0:
		cur_cnt-=1
		string[cur_idx]=cur_color
		cur_idx+=2 
	cur_cnt,cur_color=colors.pop()
	#print (string,cur_cnt,cur_color,cur_idx)
	while cur_cnt>0:
		cur_cnt-=1
		string[cur_idx]=cur_color
		cur_idx+=2 
	return ''.join(string)




def solve(N,R,O,Y,G,B,V):
	
	string=calc(N,R,Y,B)
	if string is None: return 'IMPOSSIBLE'
	
	return string 

if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		N=int(next(in_f)[:-1])
		for i in range(N):
			N,R,O,Y,G,B,V=tuple(map(int,next(in_f).split()))
			out_f.write("Case #%i: %s\n" %(i+1,solve(N,R,O,Y,G,B,V)))
				
	        