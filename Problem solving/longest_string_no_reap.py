# Find longest sub-string for which no repeated charecter
import pdb

s = 'abvasdfghjkl;!@#$%^&*()'

def check_repeat(s, start, end):
    temp={}
    for i in range(start, end):
        if s[i] in temp.keys():
            return True
        else:
            temp[s[i]] = 1

    return False

def slide_substring(s):
    window=len(s)
    while(window>1):
        start = 0
        while(start+window <= len(s)):
            if not check_repeat(s, start, start+window):
                return s[start:start+window]
            start+=1
        window -= 1
    return s[0]

print(slide_substring(s))
