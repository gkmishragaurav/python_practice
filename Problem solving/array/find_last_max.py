# This question was asked in DP world online test.
# Given an array arr[] consisting of N integers, rearrange the array such that it satisfies the following conditions:
# arr[0] must be 1.
# Difference between adjacent array elements should not exceed 1, that is, arr[i] – arr[i-1] ≤ 1 for all 1 ≤ i < N.
# The permissible operations are as follows:
# Rearrange the elements in any way.
# Reduce any element to any number ≥ 1.
# The task is to find the maximum possible value that can be placed at the last index of the array.
# Examples:
# Input: arr[] = {3, 1, 3, 4}
# Output: 4
# Explanation:
# Subtracting 1 from the first element modifies the array to {2, 1, 3, 4}.
# Swapping the first two elements modifes the array to {1, 2, 3, 4}.
# Therefore, maximum value placed at the last index is 4.

def find_last_max(a):
    a.sort()
    if a[0] != 1:
        a[0] = 1
    i=1
    while i<len(a):
        if a[i]-a[i-1] > 1:
            a[i] = a[i-1]+1
        i=i+1

    return a[-1]

a=[1, 1, 1, 1]

print(find_last_max(a))
