

import sys
from math import *
from heapq import *
from fractions import gcd
from collections import *
from sys import stderr
import bisect


def get_int(f):
    return int(next(f)[:-1])
def get_ints(f):
    return tuple(map(int,next(in_f).split()))
def get_list(f):
    return list(map(int,next(in_f).split()))
def get_ints_list(f,N):
    return [list(map(int,next(in_f).split())) for _ in range(N)]

# Find the maximum amount of overlap. We can just try
# every possible amount and check which ones work.
def max_overlap(t):
  for i in range(1, len(t)):
    if t[i:] == t[0:len(t)-i]:
      return len(t) - i
  return 0

# Returns the probability of the target word
# occurring at a fixed place.
def probability(target, keyboard):
  P = 1.0
  # Compute the product of the probabilities 
  # for each letter of the word being correct.
  for i in range(len(target)):
    # The probability for a single letter being correct
    # is the fraction of keys which are that letter.
    C = keyboard.count(target[i])
    P = P * C / len(keyboard);
  return P
def solve(K,L,S,keyboard,target):
    P = probability(target, keyboard)
    res=0
    if P > 0:
        O = max_overlap(target)
        max_copies = 1.0 + (S-L) // (L-O)
        min_copies = P * (S-L+1)
        res = max_copies - min_copies

    return res

if __name__ == "__main__":
    in_file=sys.argv[1]
    out_file=sys.argv[2]
    with open(in_file,'r') as in_f, open(out_file,'w') as out_f:
        cases=int(next(in_f)[:-1])
        for i in range(cases):
            K,L,S=get_ints(in_f)
            keyboard=next(in_f)[:-1]
            target=next(in_f)[:-1]
            out_f.write("Case #%i: %f\n" %(i+1,solve(K,L,S,keyboard,target)))
            

            
             

