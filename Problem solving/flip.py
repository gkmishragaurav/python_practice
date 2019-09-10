# Maximize number of 0s by flipping a subarray
#
# Given a binary array, find the maximum number zeros in an array with one flip of a subarray allowed. A flip operation switches all 0s to 1s and 1s to 0s.
#
# Examples:
#
# Input :  arr[] = {0, 1, 0, 0, 1, 1, 0}
# Output : 6
# We can get 6 zeros by flipping the subarray {1, 1}
#
# Input :  arr[] = {0, 0, 0, 1, 0, 1}
# Output : 5

def flip(a):
    # a loop to count all zero
    # if a one appear start a j to take count till next zero, at any point save diff if value is max.
    i=0;count=0;j=0; max=0
    while(i<len(a)):
        if a[i] == 0:
            count=count+1
            j=0
            i=i+1
        else:
            j=j+1
            i=i+1
            if j> max:
                max = j

    return max + count

arr = [0, 0, 0, 1, 0, 1]
print flip(arr)