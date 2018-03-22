#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import collections
import math
def solve(N,P,G):
	cnt_dict=collections.defaultdict(int)
	for g in G:
		cnt_dict[g%P]+=1
	ret=cnt_dict[0]
	if P==2:
		ret += math.ceil(cnt_dict[1]/2)
	if P==3:
		ret += min(cnt_dict[1],cnt_dict[2])+math.ceil(abs(cnt_dict[1]-cnt_dict[2])/3)
	if P==4:
		ret += math.floor(cnt_dict[2]/2)+min(cnt_dict[1],cnt_dict[3])
		extra=abs(cnt_dict[1]-cnt_dict[3])
		if cnt_dict[2]%2==1:
			ret+=1
			ret+=math.ceil(max(0,extra-2)/4)
		else:
			ret+=math.ceil(extra/4)

	return ret




	
if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		cases=int(next(in_f)[:-1])
		for i in range(cases):
			N,P =tuple(map(int,next(in_f).split()))
			G=list(map(int,next(in_f).split()))
			out_f.write("Case #%i: %i\n" %(i+1,solve(N,P,G)))
			
		
	        