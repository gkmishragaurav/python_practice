# You are given an integer array coins representing coins of different denominations and an integer amount 
# representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.


import time
def sol(a, n, pos, s):
    if n==0:
        print('ans',s)
        if ans[0] > s:
            ans[0]=s
        return 1

    if pos == len(a) or n<0:
        return 0

    s=s+1
    key=(n-a[pos], pos)
    if key not in d:
        incl = sol(a, n-a[pos], pos, s)
        s=s-1
        excl = sol(a, n, pos+1, s)

        d[key]=incl+excl

    return d[key]

d={}
ans=[float('inf')]
a=[1,2,2,5]
t1=time.time()
a.sort(reverse=False)
print(a)
x=sol(a, 7, 0, 0)
t2=time.time()
print('>>>>>>>>',x, ans, t2-t1)

