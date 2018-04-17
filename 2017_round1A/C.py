#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import math
def calc(b,B,hd,ad,hk,ak,Hd):
	rnd=0
	for i in range(b):
		if hd<ak:
			hd=Hd-ak
			rnd+=1 
		ad+=B
		hd-=ak 
		rnd+=1 
	while 1:
		if hk<=ad: return rnd+1
		if hd<=ak: 
			hd=Hd-ak
			rnd+=1 
		hk-=ad 
		hd-=ak 
		rnd+=1 
	return rnd 



def simulate(Hd,Ad,Hk,Ak,B,D,d):
	#return min number of rounds needed to defeat knight, with d debuffs 
	rnd=0
	hd=Hd
	ak=Ak
	for i in range(d):
		if hd<=ak: 
			#cure 
			hd=Hd-ak
			rnd+=1 
		#debuff 
		ak-=D
		hd-=ak 
		rnd+=1 
	# current state hd,Ad,Hk,ak 
	if hd<=2*ak: #只能承受一轮攻击 需要不断医疗
		return float('inf')
	if B==0: 
		return rnd+calc(0,B,hd,Ad,Hk,ak,Hd)
	else:
		min_buff_attack=float('inf')
		while 1:
			b=0
			buff_attack=calc(b,B,hd,Ad,Hk,ak,Hd)
			if buff_attack>min_buff_attack:
				break 
			min_buff_attack=buff_attack
			b+=1 
	return rnd+min_buff_attack





def solve(Hd,Ad,Hk,Ak,B,D):
	if Hd<=Ak and Hd<=(Ak-D): return 'IMPOSSIBLE'
	if Hd<=2*Ak: # 只能承受一次攻击
		if 2*(Ak-D)>=Hd: #debuff 之后也还是只能承受一次攻击
			if Ad+B<Hk:
				return 'IMPOSSIBLE' #buff 之后也不能打死kight 
			else: return 2 #buff, 挨打， 攻击， 结束
		else:
			d=1 #至少debuff 一次
	k=Hd//Ak # need to cure every k round
	if D==0: 
		debuff=[0] 
	else:
		debuff=[]
		d=0
		while d*D<Ak:
			debuff.append(d)
			k+=1
			d=math.ceil((Ak-(Hd-0.1)/k)/D)
	ret=float('inf')
	for d in debuff:
		ret=min(ret,simulate(Hd,Ad,Hk,Ak,B,D,d))
	if ret==float('inf'):
		return 'IMPOSSIBLE'
	return ret 

if __name__ == "__main__":
	in_file=sys.argv[1]
	out_file=sys.argv[2]
	with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
		N=int(next(in_f)[:-1])
		for i in range(N):
			Hd,Ad,Hk,Ak,B,D=tuple(map(int,next(in_f).split()))
			out_f.write("Case #%i: %s\n" %(i+1,solve(Hd,Ad,Hk,Ak,B,D)))
				
	        