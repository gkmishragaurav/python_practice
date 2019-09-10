# needle in haystack
import pdb
def compare(s1, s2):
    i=0
    while(i<len(s2)):
        if s1[i] != s2[i]:
            return False
        else:
            i=i+1
    return True

def strstr(s1, s2):
    if not s1 or not s2: return -1
    i=0
    if len(s1) >= len(s2):
        while(i<len(s1)-len(s2)+1):
            status = compare(s1[i:], s2)
            # print status
            if status:
                return i
            else:
                i=i+1
    return -1

def strstr1(s1, s2):
    # Another variation of above mathod.
    if not s1 or not s2: return -1
    if len(s1) > len(s2):
        i=0;j=0
        while(i<len(s1)): # twick it with right length
            if s1[i] == s2[j]:
                if j == len(s2)-1:
                    return i-j
                j = j + 1
            else:
                j=0
            i = i + 1
    return -1


needle = 'abc'
haystack = 'abc'

print strstr(haystack, needle)