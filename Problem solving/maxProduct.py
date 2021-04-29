# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product,
# and return the product.
# It is guaranteed that the answer will fit in a 32-bit integer. A subarray is a contiguous subsequence of the array.
# Example 1:
#
# Input: nums = [2,3,-2,4]
# Output: 6
# Explanation: [2,3] has the largest product 6.
# Example 2:
#
# Input: nums = [-2,0,-1]
# Output: 0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

def maxProduct(a) -> int:
    curr_max_pro = 1
    curr_min_pro = 1
    max_pro = float('-inf')
    min_pro = float('inf')
    i=0
    while i<len(a):
        temp = curr_max_pro*a[i]
        curr_max_pro=max(curr_max_pro*a[i], curr_min_pro*a[i])
        if curr_max_pro > max_pro:
            max_pro=curr_max_pro

        if curr_max_pro <= 0:
            curr_max_pro=1

        curr_min_pro=min(curr_min_pro*a[i], temp)

        if curr_min_pro < min_pro:
            min_pro = curr_min_pro

        if curr_min_pro >= 0:
            curr_min_pro = 1

        i=i+1
    print(max_pro, min_pro)
    return max_pro

print(maxProduct([2,-5,1,-4,3,-2]))
