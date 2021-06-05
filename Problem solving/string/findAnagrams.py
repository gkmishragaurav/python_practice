# Given two strings s and p, return an array of all the start indices of p's anagrams in s. 
# You may return the answer in any order.

def make_dict(str):
    d={}
    for item in str:
        if item not in d:
            d[item]=0
        d[item]=d[item]+1
    return d

def findAnagrams(s, p):
    ans=[]
    n=len(p)
    p=make_dict(p)
    temp = make_dict(s[:n])
    i=0
    while i+len(p)<=len(s):
        print('ans-', ans)
        if i+len(p) == len(s):
            if temp == p:
                ans.append(i)
            break

        if temp == p:
            ans.append(i)
        i=i+1

        # remove previous
        print('removing-',s[i-1])
        if temp[s[i-1]] == 1:
            del temp[s[i-1]]
        else:
            temp[s[i-1]] = temp[s[i-1]]-1

        # add new
        new=i+n-1
        if new<len(s):
            print('adding-',s[new])
            if s[new] not in temp:
                temp[s[new]] = 1
            else:
                temp[s[new]] = temp[s[new]]+1

    return ans

s = "cbaebabacdcbaebabacd"
p = "cbaebabacd"
x=findAnagrams(s, p)
print(x)
