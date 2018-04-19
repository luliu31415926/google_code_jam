import sys
import math
import collections 

def maximize(s):
    return ''.join(['9' if c=='?' else c for c in s])



def minimize(s):
    return ''.join(['0' if c=='?' else c for c in s])



def solve(c,j):
    N=len(c)
    cand=[]
    ret_common=''
    for i in range(N):
        if c[i]==j[i]=='?':
            cand.append((ret_common+'1'+minimize(c[i+1:]),ret_common+'0'+maximize(j[i+1:])))
            cand.append((ret_common+'0'+maximize(c[i+1:]),ret_common+'1'+minimize(j[i+1:])))
            ret_common+='0'
        elif c[i]=='?':
            if j[i]!='9':
                cand.append((ret_common+str(int(j[i])+1)+minimize(c[i+1:]),ret_common+j[i]+maximize(j[i+1:])))
            if j[i]!='0':
                cand.append((ret_common+str(int(j[i])-1)+maximize(c[i+1:]),ret_common+j[i]+minimize(j[i+1:])))
            ret_common+=j[i]
        elif j[i]=='?':
            if c[i]!='9':
                cand.append((ret_common+c[i]+maximize(c[i+1:]),ret_common+str(int(c[i])+1)+minimize(j[i+1:])))
            if c[i]!='0':
                cand.append((ret_common+c[i]+minimize(c[i+1:]),ret_common+str(int(c[i])-1)+maximize(j[i+1:])))
            ret_common+=c[i]
        elif c[i]==j[i]:
            ret_common+=c[i]
        elif int(c[i])>int(j[i]):
            cand.append((ret_common+c[i]+minimize(c[i+1:]),ret_common+j[i]+maximize(j[i+1:])))
            break
        else:
            cand.append((ret_common+c[i]+maximize(c[i+1:]),ret_common+j[i]+minimize(j[i+1:])))
            break 
    if len(ret_common)==N:
        return ret_common,ret_common
    cand.sort()
    cand.sort(key=lambda x:abs(int(x[0])-int(x[1])))
    return cand[0]


if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            coder,jammer=next(in_f).split()
            c_ret,j_ret=solve(coder,jammer)
            out_f.write("Case #%i: %s %s\n" %(i+1,c_ret,j_ret))
             

