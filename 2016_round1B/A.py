import sys
import math
import collections 


def solve(S):
    c=collections.Counter(S)
    ret=[]
    if 'Z' in c:
        ret+=[0]*c['Z']
        for l in 'ERO':
            c[l]-=c['Z']
            if c[l]==0: del c[l]
        del c['Z']

    if 'W' in c:
        ret+=[2]*c['W']
        for l in 'TO':
            c[l]-=c['W']
            if c[l]==0: del c[l] 
        del c['W'] 

    if 'U' in c:
        ret+=[4]*c['U']
        for l in 'FOR':
            c[l]-=c['U']
            if c[l]==0: del c[l] 
        del c['U']
    if 'F' in c:
        ret+=[5]*c['F']
        for l in 'IVE':
            c[l]-=c['F']
            if c[l]==0: del c[l] 
        del c['F']
    if 'X' in c:
        ret+=[6]*c['X']
        for l in 'SI':
            c[l]-=c['X']
            if c[l]==0: del c[l] 
        del c['X']
    if 'V' in c:
        ret+=[7]*c['V']
        for l in 'SEEN':
            c[l]-=c['V']
            if c[l]==0: del c[l] 
        del c['V']
    if 'G' in c:
        ret+=[8]*c['G']
        for l in 'EIHT':
            c[l]-=c['G']
            if c[l]==0: del c[l] 
        del c['G']
    if 'I' in c:
        ret+=[9]*c['I']
        for l in 'NNE':
            c[l]-=c['I']
            if c[l]==0: del c[l] 
        del c['I']

    if 'O' in c:
        ret+=[1]*c['O']
        for l in 'NE':
            c[l]-=c['O']
            if c[l]==0: del c[l] 
        del c['O']
    ret+=[3]*c['T']
    return ''.join(map(str,sorted(ret)))
    

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            S=next(in_f)[:-1]
            out_f.write("Case #%i: %s\n" %(i+1,solve(S)))
             

