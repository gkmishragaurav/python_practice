# Given an integer array nums, return the length of the longest strictly increasing subsequence.
# 
# A subsequence is a sequence that can be derived from an array by deleting some or no elements without changing the order of the remaining elements. For example, [3,6,2,7] is a subsequence of the array [0,3,1,6,2,2,7].
# 

import time
def sol(a, pos, s):
    if pos==len(a):
        return

    if not s or s[-1] <= a[pos]:
        s.append(a[pos])
        if len(s)>maxi[0]:
            maxi[0] = len(s)

    key = (pos+1, tuple(s))
    if key not in d:
        d[key]=sol(a, pos+1, s)
    if s:
        s.pop()
    key = (pos+1, tuple(s))
    if key not in d:
        sol(a, pos+1, s)

d={}
t1=time.time()
maxi=[0]
a=[10,9,2,5,3,7,101,18,10,9,2,5,3,7,101,18,10,9,2,5,3,6, 10,9,2,5,3,7,101,18,10,9,2,5,3,7,101,18,10,9,2,5,3,6,10,9,2,5,3,7,101,18,10,9,2,5,3,7,101,18,10,9,2,5,3,6,10,9,2,5,3,7,101,18,10,9,2,5,3,7,101,18,10]
print(len(a))
sol(a, 0, [])
t2=time.time()
print(maxi, t2-t1)


