# Given the array nums, for each nums[i] find out how many numbers in the array
# are smaller than it. That is, for each nums[i] you have to count the number of
# valid j's such that j != i and nums[j] < nums[i].
#
# Return the answer in an array.
import copy

nums = [8,1,2,2,3]
x = [1,2,2,3,8]

def smallerNumbersThanCurrent(nums):
  temp = copy.deepcopy(nums)
  temp.sort()
  ans=[]
  for item in nums:
    ans.append(temp.index(item))
  return ans

print smallerNumbersThanCurrent(nums)
