def is_noRepeat(s):
    print(s)
    d={}
    i=0
    while i<len(s):
        if s[i] not in d:
            d[s[i]] = 0
        else:
            return False
        i=i+1

    return True

def lengthOfLongestSubstring(s):
    if not s:
        return 0
    i=0
    start=end=i
    max_str=float('-inf')
    while i<len(s):
        if is_noRepeat(s[start:i+1]):
            end=i+1
            if end-start > max_str:
                max_str = end-start
        else:
            start=start+1
        i=i+1

    return max_str

s='dvdf'
print(lengthOfLongestSubstring(s))
