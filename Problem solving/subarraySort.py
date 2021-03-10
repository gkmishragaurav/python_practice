# Write a function that takes an array of at least 2 integers and returns 
# an array of starting and ending indicies of the smallest subarray in the 
# input array that needs to be sorted in place in order for the entire input 
# array to be sorted, sample inputs are given below.

def subarraySort(a):
    i=0
    find_last = False
    start = -1
    end = -1
    start_index=None
    while i < len(a)-1:
        if a[i] > a[i+1]:
            start_index = i+1
            last_max = a[i]
            find_last = True
            break
        i=i+1

    if find_last:
        while i < len(a):
            if a[i] <= last_max:
                end = i

            i=i+1

    # find minimum b/w start and end
    if start_index:
        i=start_index
        minimum = a[i]
        maxi = float('-inf')
        while i<=end:
            if minimum > a[i]:
                minimum = a[i]

            if maxi < a[i]:
                maxi = a[i]
            i=i+1

    i=0
    if start_index:
        while(i<start_index):
            if a[i] > minimum:
                start = i
                break
            i=i+1

    if end != -1:
        i=end
        while(i<len(a)):
            if a[i] < maxi:
                end = i

            i=i+1

    return start, end
#sample inputs
# a=[1, 2, 4, 7, 10, 11, 7, 12, 6, 7, 16, 18, 19] #3,9
# a=[2, 1] #0,1
# a=[1,2] # -1,-1
a= [1, 2, 4, 7, 10, 11, 7, 12, 7, 7, 16, 18, 19] # 4,9
# a=[4, 8, 7, 12, 11, 9, -1, 3, 9, 16, -15, 11, 57] # 0,11
print(subarraySort(a))
