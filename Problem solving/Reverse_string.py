def reverse_str(a):
    i=len(a)-1
    str=''
    while(i>=0):
        str=str+a[i]
        i=i-1

    return str

s = 'Today is a good day'
# day good a is Today.
arr = s.split(' ')
i=0;j=len(arr)-1
while(j>i):
    arr[i], arr[j] = arr[j], arr[i]
    i=i+1
    j=j-1

str=''
for x in arr:
    str = str + x +' '

print str

# s = reverse_str(s)
# arr = s.split(' ')
# str=''
# for x in arr:
#     str = str + reverse_str(x) + ' '
# print str
