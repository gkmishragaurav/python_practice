# Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two
# whose elements sum up to a multiple of k, or false otherwise.

####### Example 1:
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.


def find_sum(nums, start, k, ans):
  if k == 0:
    return True, ans
  if start > len(nums)-1:
    return False
  ans.append(nums[start])
  return find_sum(nums, start+1, k-nums[start], ans)

nums = [23,2,4,6,7]
k = 6
for i in range(len(nums)):
  ans = []
  temp = find_sum(nums, i, k, ans)
  if temp and len(temp[1]) > 1:
      print(ans)
