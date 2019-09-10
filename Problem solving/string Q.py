##### Smallest window that contains all characters of string itself
# Input  : aabcbcdbca
# Output : dcba

string = "aabcbcdbcaqwertyuiop"

def is_distinct(str):
    d={}
    for i in range(len(str)):
        if str[i] in d.keys():
            return False
        else:
            d[str[i]] = None
    return True

i=0
j=1
max=0

while j <= len(string):
    print i, string[i:j]
    print is_distinct(string[i:j])
    if is_distinct(string[i:j]):
        if j-1 > max:
            max = j-i
        j=j+1
    else        i=i+1

print 'final length-', max