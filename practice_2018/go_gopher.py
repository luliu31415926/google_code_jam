import math
t=int(input())
need_debug=False
for _ in range(t):
	A=int(input())
	max_len=math.ceil(A/3)

	planted=[[0,0,0,0] for _ in range(max_len+5) ]

	cur_i,cur_j=2,2
	print (cur_i,cur_j)
	pi,pj=tuple(map(int,input().split()))
	while pi!=0:
		planted[pi][pj]=1
		if sum(planted[cur_i-1])==3 and cur_i<max_len-1: cur_i+=1 
		print (cur_i,cur_j)
		pi,pj=tuple(map(int,input().split()))
		if pi==-1: 
			need_debug=True
			print ('need_debug')
			break 
	if need_debug:
		break
