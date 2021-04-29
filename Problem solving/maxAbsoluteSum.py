#You are given an integer array nums. The absolute sum of a subarray [numsl, numsl+1, ..., numsr-1, numsr] is
# abs(numsl + numsl+1 + ... + numsr-1 + numsr).
# Return the maximum absolute sum of any (possibly empty) subarray of nums.
# Note that abs(x) is defined as follows:
# If x is a negative integer, then abs(x) = -x.
# If x is a non-negative integer, then abs(x) = x.
# Input: nums = [2,-5,1,-4,3,-2]
# Output: 8
# Explanation: The subarray [-5,1,-4] has absolute sum = abs(-5+1-4) = abs(-8) = 8.

def maxAbsoluteSum(nums) -> int:
    min_sum=float('inf')
    max_sum=float('-inf')
    i=0
    curr_sum_max=0
    curr_sum_min=0
    while i<len(nums):
        curr_sum_max=curr_sum_max+nums[i]
        if curr_sum_max > max_sum:
            max_sum = curr_sum_max
        if curr_sum_max<0:
            curr_sum_max=0

        curr_sum_min=curr_sum_min+nums[i]
        if curr_sum_min < min_sum:
            min_sum = curr_sum_min
        if curr_sum_min>0:
            curr_sum_min=0
        i=i+1

    return max(abs(min_sum), max_sum)

print(maxAbsoluteSum([2,-5,1,-4,3,-2]))
