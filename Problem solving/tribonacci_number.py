# The Tribonacci sequence Tn is defined as follows: 
# T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
# Given n, return the value of Tn.

import functools
class Solution:
    def cache(func):
        """Keep a cache of previous function calls"""
        @functools.wraps(func)
        def wrapper_cache(*args, **kwargs):
            cache_key = args + tuple(kwargs.items())
            if cache_key not in wrapper_cache.cache:
                wrapper_cache.cache[cache_key] = func(*args, **kwargs)
            return wrapper_cache.cache[cache_key]
        wrapper_cache.cache = dict()
        return wrapper_cache
    
    @cache
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        
        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)
