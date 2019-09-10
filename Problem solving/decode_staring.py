s='a30b4c3'
# aaabbbbccc

stack=''
i=0

while(i<len(s)):
    st = s[i]
    num=0;i=i+1
    while(48<=ord(s[i])<=57):
        num=num*10+int(s[i])
        i=i+1
        if i == len(s):
            break
    stack = stack + st * num

print stack