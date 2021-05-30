# We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
# Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences.
# A subsequence of array is a sequence that can be derived from the array by deleting some or no elements without changing 
# the order of the remaining elements.
# Example 1:
# Input: nums = [1,3,2,2,5,2,3,7]
# Output: 5
# Explanation: The longest harmonious subsequence is [3,2,2,2,3].

def findLHS(a):
    d={}
    ans=0
    for item in a:
        num1=0;num2=0
        if item not in d:
            d[item]=0
        d[item]=d[item]+1
        if item-1 in d:
            num1=d[item-1]+d[item]
        if item+1 in d:
            num2=d[item+1]+d[item]
        if max(num1,num2) > ans:
            ans = max(num1, num2)

    return ans

# a=[1,3,2,2,5,2,3,7]
# a = [1,2,3,4]
a=[1,1,1,1]
x = findLHS(a)
print(x)
