# Reverse a string - without any inbuild fuction - strrev

def strrev1(s):
    # if we can use extra space, in python, deletion of a character is not allowed.
    temp=''
    i=len(s)-1
    while(i>=0):
        temp=temp+s[i]
        i=i-1
    return temp


print strrev1('abcdefghijk')