# Given an array nums of n integers where nums[i] is in the range [1, n],
# return an array of all the integers in the range [1, n] that do not appear in nums.
# Example 1:
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]

def findDisappearedNumbers(nums):
    for item in nums:
        temp=abs(item)
        if nums[temp-1]>0:
            nums[temp-1] = -nums[temp-1]

    ans=[]
    for i, item in enumerate(nums):
        if item>0:
            ans.append(i+1)

    return ans

x=findDisappearedNumbers([4,3,2,7,8,2,3,1,9,10,11,12,13,15,16,3,5,12])
print(x)
