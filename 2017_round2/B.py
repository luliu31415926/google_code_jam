#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import collections
import math


def solve(N,C,M,tickets):
	# N: number of seats in each ride
	# C: number of potential customers 1 to C
	# M: number of tickets sold 
	# tickets: [(position, buyer)]
	# return min number of rides and min number of promotions
	customer_dict=collections.defaultdict(list)
	tickets_dict=collections.defaultdict(int)
	for p,c in tickets:
		customer_dict[c].append(p)
		tickets_dict[p]+=1
	rides=max(len(val) for key,val in customer_dict.items()) 
	empty_seats=0 #initialize empty seats available for ticket position 1
	promos=0 # count number of promotions need to be done 
	#print ('customers',customer_dict)
	#print ('tickets',tickets_dict)
	#print ('row, rides, promos, empty_seats')
	for i in range(1,N+1):
		# analyse each row 
		empty_seats+=rides # add a new row of empty seats 
		if tickets_dict[i]>empty_seats:
			add_ride=math.ceil((tickets_dict[i]-empty_seats)/i) #each new ride add i empty seats
			#print ('add new ride',add_ride)
			rides+=add_ride
			empty_seats=empty_seats+add_ride*i- tickets_dict[i]
		else:
			empty_seats-=tickets_dict[i]
		promos+=max(0,tickets_dict[i]-rides)
		#print (i,rides, promos,empty_seats)

	return rides,promos

	
if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		cases=int(next(in_f)[:-1])
		for i in range(cases):
			N,C,M =tuple(map(int,next(in_f).split()))
			tickets=[tuple(map(int,next(in_f).split())) for r in range(M)]
			rides,promos=solve(N,C,M,tickets)
			out_f.write("Case #%i: %i %i\n" %(i+1,rides,promos))
			
			
		
	        