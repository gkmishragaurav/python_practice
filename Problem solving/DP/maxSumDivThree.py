# Given an array nums of integers, we need to find the maximum possible sum of elements of the array such that it is divisible by three.

maxi = [0]
def maxSumDivThree(a, pos, s):
    if pos >=len(a):
        return
    s.append(a[pos])
    temp = sum(s)
    if temp%3==0 and temp>maxi[0]:
        maxi[0] = temp

    key = (pos+1, temp)
    if key not in d:
        d[key] = maxSumDivThree(a, pos+1, s)

    t1 = s.pop()

    key = (pos+1, temp-t1)
    if key not in d:
        d[key] = maxSumDivThree(a, pos+1, s)


import time
d={}
# a=[3,6,5,1,8,3,4,5,6,7,7,8,9,2,3,4,5,6,7,8,9,1,1,1,2,4,5,7,8]
a=[3,6,5,1,8,3,4,5,6,7,7,8,9,2,3,4,5,6,7,8,9,1,3]
t1=time.time()
x=maxSumDivThree(a,0, [])
t2=time.time()
print(maxi, max(maxi))
print(t2-t1)
