#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
def solve(D,data):
	ret=float('inf')

	data.sort(key=lambda x: -x[0])
	for k,s in data:
		ret=min(ret,D*s/(D-k))
	return ret 
if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		cases=int(next(in_f)[:-1])
		for i in range(cases):
			D,N =tuple(map(int,next(in_f).split()))
			data=[tuple(map(int,next(in_f).split())) for j in range(N)]
			out_f.write("Case #%i: %.6f\n" %(i+1,solve(D,data)))
			
		
	        