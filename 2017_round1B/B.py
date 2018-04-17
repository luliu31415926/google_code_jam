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

	if (N==(B+O) and B==O):
		return 'BO'*O
	if (N==(R+G) and R==G):
		return 'RG'*G
	if (N==(Y+V) and Y==V):
		return 'YV'*V
	if (O>0 and B<O+1) or (V>0 and Y<V+1) or (G>0 and R<G+1): 
		print ('not enough primary colors ')
		return 'IMPOSSIBLE'
	string=calc(N-2*O-2*V-2*G,R-G,Y-V,B-O)
	if string is None: return 'IMPOSSIBLE'
	if O>0:
		p=string.index('B')
		string=string[:p]+'BO'*O+string[p:]
	if V>0:
		p=string.index('Y')
		string=string[:p]+'YV'*V+string[p:]
	if G>0:
		p=string.index('R')
		string=string[:p]+'RG'*G+string[p:]
	return string 

if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		N=int(next(in_f)[:-1])
		for i in range(N):
			N,R,O,Y,G,B,V=tuple(map(int,next(in_f).split()))
			out_f.write("Case #%i: %s\n" %(i+1,solve(N,R,O,Y,G,B,V)))
				
	        