# hacker rank in a string problem

def hackerrankInString(s, base):
    i=0 #for s
    j=0 #for base
    found=0
    if len(s) < len(base):
        return 'NO'
    else:
        while(i<(len(s))):
            if base[j] == s[i]:
                i=i+1;j=j+1;found=found+1
            else:
                i=i+1
            if found == len(base):
                return 'Yes'
    return 'NO'


base='hackerrank'
str='hackerworld'

print hackerrankInString(str, base)