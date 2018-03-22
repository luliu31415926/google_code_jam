#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
def solve(line):
	pancakes, k=line.split()
	L=len(pancakes)
	pancake_mask=0
	for i,p in enumerate(pancakes):
		if p=='+':
			pancake_mask|=(1<<(L-i-1))

	k=int(k)
	cnt=0
	cur=0
	flipper=(1<<k)-1
	while cur<L-k+1:
		if pancake_mask & 1<<cur == 0: 
			pancake_mask^=(flipper<<cur)
			cnt+=1	
		cur+=1 
	if pancake_mask>>(cur-1) ==flipper :
		return cnt
	else: 
		return -1



if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		for i, line in enumerate(in_f):
			if i==0: continue 
			ret=solve(line)
			if ret==-1:
				out_f.write("Case #%i: %s\n" % (i, 'IMPOSSIBLE'))
			else:
				out_f.write("Case #%i: %i\n" % (i, ret))
		
	        