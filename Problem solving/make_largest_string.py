# Arrange given numbers to form the biggest number

# Given an array of numbers, arrange them in a way that yields the largest value.
# For example, if the given numbers are {54, 546, 548, 60}, the arrangement 6054854654 gives the largest value.
# And if the given numbers are {1, 34, 3, 98, 9, 76, 45, 4}, then the arrangement 998764543431 gives the largest value.

def make_largest_string(a):
    str1 = ''
    temp = my_sort(a)
    for i in range(len(temp)):
        str1=str1+str(temp[i])
    return str1

def my_sort(a):
    all_zero = False
    if len(a) == 1: return a
    else:
        for j in range(len(a)):
            i=0
            while(i<len(a)-1):
                if a[i] == 0:
                    all_zero = True
                if str(a[i])+ str(a[i+1]) < str(a[i+1])+str(a[i]):
                    a[i],a[i+1] = a[i+1],a[i]
                i=i+1
    if all_zero: return 0
    return a

a = [0, 34, 3, 98, 9, 76, 45, 4]
# a=[0,0,0,0]
print make_largest_string(a)
