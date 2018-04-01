import math
t=int(input())
need_debug=False
for _ in range(t):
	A,B=tuple(int(s) for s in input().split())
	N=int(input())
	while N>0:
		guess=A+math.ceil((B-A)/2)
		print (guess)
		N-=1
		ret=input()
		if ret=='CORRECT': break
		elif ret=='TOO_SMALL':	A=guess
		elif ret=='TOO_BIG': B=guess-1 
		else: 
			need_debug=True
			break
	if need_debug:
		break

