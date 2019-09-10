# https://leetcode.com/problems/perfect-squares/
# Given a positive integer n, find the least number of perfect
# square numbers (e.g., 1, 4, 9, 16, ...) which sum to n.
import time
import pdb
from functools import wraps
#python2
def cache(function):
    memo = {}
    @wraps(function)
    def wrapper(*args):
        try:
            return memo[args]
        except KeyError:
            rv = function(*args)
            memo[args] = rv
            return rv
    return wrapper

@cache
def perfect_square(n):
    if n <= 3:
        return n
    count=n
    for num in range(1, n+1):
        temp = num**2
        if temp>n:
            break
        else:
            count = min(1+perfect_square(n-temp), count)
    return count
t1=time.time()
print perfect_square(45)
t2=time.time()
print t2-t1

#2
# 3.98900008202

