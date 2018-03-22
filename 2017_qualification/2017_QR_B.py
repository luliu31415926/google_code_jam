#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
def solve(line):
	if len(line)==1: return int(line)
	num=[int(d) for d in line[:-1]]
	cur=0
	while cur<len(num)-1:
		if num[cur]<=num[cur+1]:
			cur+=1 
		else:
			num[cur]-=1
			num[cur+1:]=[9]*(len(num)-cur-1)
			break
	while cur>0:
		if num[cur]>=num[cur-1]:break
		else:
			num[cur-1]-=1
			num[cur]=9
			cur-=1
	return int(''.join(map(str,num)))



if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		for i, line in enumerate(in_f):
			if i==0: continue 
			ret=solve(line)
			out_f.write("Case #%i: %i\n" % (i, ret))
		
	        