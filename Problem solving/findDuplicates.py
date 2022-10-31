# Given an integer array nums of length n where all the integers of nums are in the range [1, n]
# and each integer appears once or twice, return an array of all the integers that appears twice.
# You must write an algorithm that runs in O(n) time and uses only constant extra space.


nums = [4,3,2,7,8,2,3,1]

def findDuplicates(nums):
  ans=[]
  for i in range(len(nums)):
    index = abs(nums[i])-1
    if nums[index]<0:
      ans.append(index+1)
    else:
      nums[index] = -nums[index]
  return ans

print(findDuplicates(nums))
