#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
def solve(cake,R,C):
	cur_x=0
	while cur_x<R:
		start=0
		cur_y=0
		cur_initial=None
		while cur_y<C :
			if cake[cur_x][cur_y]!='?' and cur_initial is None:
				cur_initial=cake[cur_x][cur_y]
			elif cake[cur_x][cur_y]!='?' and cur_initial is not None:
				cake[cur_x]=cake[cur_x][:start]+cur_initial*(cur_y-start)+cake[cur_x][cur_y:]
				start=cur_y
				cur_initial=cake[cur_x][cur_y]
			cur_y+=1
		if cur_initial is not None:
			cake[cur_x]=cake[cur_x][:start]+cur_initial*(cur_y-start)+cake[cur_x][cur_y:]
		cur_x+=1
	cur_line=None
	for i in range(R):
		if cake[i][0]!='?':
			cur_line=cake[i]
			break
	cur_x=0
	while cur_x<R:
		if cake[cur_x][0]=='?':
			cake[cur_x]=cur_line
		else:
			cur_line=cake[cur_x]
		cur_x+=1 


	return cake

if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		N=int(next(in_f)[:-1])
		for i in range(N):
			RC=tuple(map(int,next(in_f).split()))
			cake=[]
			for j in range(RC[0]):
				cake.append(next(in_f)[:-1])
			solved_cake=solve(cake,RC[0],RC[1])
			out_f.write("Case #%i:\n" %(i+1))
			for c in solved_cake:
				out_f.write(c+'\n')
		
	        