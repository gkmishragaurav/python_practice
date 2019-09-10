# Minimum characters to be added at front to make string palindrome
# Given a string str we need to tell minimum characters to be added at front of string to make string palindrome.
# Input  : str = "ABC"
# Output : 2
# We can make above string palindrome as "CBABC"
# by adding 'B' and 'C' at front.
# Input  : str = "AACECAAAA";
# Output : 2
# We can make above string palindrome as AAAACECAAAA
# by adding two A's at front of string.

def ispalindrome(s):
    i=0;j=len(s)-1
    while(i<j):
        if s[i] != s[j]:
            return False
        i=i+1;j=j-1
    return True

def count_char_palindrom(s):
    i=len(s);count=0
    while(1):
        if ispalindrome(s[:i]):
            return count
        else:
            i=i-1
            count=count+1
s='aaaaaabaaaaaaerfergergetth'
count=count_char_palindrom(s)
print s[len(s)-count: len(s)][::-1]