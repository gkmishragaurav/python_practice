import functools
import time

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
def longestCommonSubsequence(text1: str, text2: str) -> int:
    if not text1 or not text2:
        return 0

    if text1[0] == text2[0]:
        return 1+ longestCommonSubsequence(text1[1:], text2[1:])

    return max(
        longestCommonSubsequence(text1[1:], text2),
        longestCommonSubsequence(text1, text2[1:]))

t1 = time.time()
x = longestCommonSubsequence("acejfnjrenjenrjknerjnjergiqeeyfugwefugqwefwcuhqwefwgvgcwrgjerpgj",
                             "abcdefrddrdsawzxdxexctfgyyhujujikopsexcfvgbzxnncvndjvwytfrqw")
t2=time.time()
print(t2-t1)
print(x)

