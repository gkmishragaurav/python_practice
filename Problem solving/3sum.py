def threeNumberSum(nums, agg):
	ts = []
	for i in range(len(nums)-2):
		item = twoSum(nums[i+1: len(nums)], agg-nums[i])
		for value in item:
			temp = [nums[i]]
			temp.extend(value)
			ts.append(sorted(temp))

	return sorted(unique(ts))

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
