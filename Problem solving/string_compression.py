# string compression

def string_compression(str1):
    temp=''
    count=1;j=1;i=0
    while(j<len(str1)):
        if str1[i] == str1[j]:
            count=count+1
        else:
            if count == 1: temp=temp+str1[i]
            else: temp=temp+str1[i]+str(count)
            count=1
        i = i + 1
        j = j + 1

    if count == 1:
        temp = temp + str1[i]
    else:
        temp = temp + str1[i] + str(count)
    return temp

str1 = 'aaaaabbbbcccdheeeeee'
print string_compression(str1)