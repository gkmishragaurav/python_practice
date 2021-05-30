# Give a binary string s, return the number of non-empty substrings that have the same number 
# of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.
# Substrings that occur multiple times are counted the number of times they occur.
# Example 1:
# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.

def countBinarySubstrings(s):
    grp = []
    i=0
    count=0
    curr = s[0]
    # make group
    while i<=len(s):
        if i==len(s):
            grp.append(count)
            break
        if s[i] == curr:
            count=count+1
        else:
            grp.append(count)
            count=1
            curr=s[i]
        i=i+1
    print(grp)
    #process group
    i=0
    ans=0
    while i<len(grp)-1:
        ans=ans+min(grp[i], grp[i+1])
        i=i+1
    return ans

s='1101111000'
x=countBinarySubstrings(s)
print(x)
