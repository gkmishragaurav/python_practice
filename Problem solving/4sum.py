# Write a function that takes a non-empty array and an integer representing a target sum. 
# That finction should find all quadruplets in the array that sum up to the target sum.

def threeNumberSum(nums, agg):
    ts = []
    for i in range(len(nums)-2):
        item = twoSum(nums[i+1: len(nums)], agg-nums[i])
        for value in item:
            temp = [nums[i]]
            temp.extend(value)
            ts.append(sorted(temp))

    return sorted(unique(ts))

def fourNumberSum(nums, agg):
    fs = []
    for i in range(len(nums)-3):
        item=threeNumberSum(nums[i+1:len(nums)], agg-nums[i])
        for value in item:
            temp = [nums[i]]
            temp.extend(value)
            fs.append(sorted(temp))

    return sorted(unique(fs))

def twoSum(nums, sum):
    all_=[]
    i=0
    e=len(nums)-1
    temp = sorted(nums)
    while(i<e):
        if temp[i]+temp[e] < sum:
            i=i+1
        elif temp[i]+temp[e] > sum:
            e=e-1
        else:
            all_.append([temp[i], temp[e]])
            i=i+1
    return all_

def unique(abc):
    temp=[]
    for item in abc:
        if item not in temp:
            temp.append(item)

    return temp

a=[7, 6, 4, -1, 1, 2]
print(fourNumberSum(a, 16))
