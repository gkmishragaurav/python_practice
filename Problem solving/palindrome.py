# Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.
#
# Example:
#
# "A man, a plan, a canal: Panama" is a palindrome.
#
# "race a car" is not a palindrome.
#
# Return 0 / 1 ( 0 for false, 1 for true ) for this problem

def palindrome(s):
    s=s.lower()
    str=''
    for x in s:
        if x >= 'a' and x <= 'z' or x>='0' and x<='9' :
            str=str+x

    i=len(s)-1
    rev=''
    while(i>=0):
        if s[i] >= 'a' and s[i] <= 'z' or x>='0' and x<='9':
            rev=rev+s[i]
        i=i-1

    if rev == str: return 1
    else: return 0

s = '1q2'
print palindrome(s)