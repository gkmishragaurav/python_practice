# Given an integer array nums of unique elements, return all possible subsets (the power set).
# The solution set must not contain duplicate subsets. Return the solution in any order.
# Example 1:
# Input: nums = [1,2,3]
# Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
import copy
def make(item, rest):
    ans = []
    i=0
    while i<len(rest):
        temp = copy.deepcopy(item)
        temp.extend([rest[i]])
        ans.append(temp)
        i=i+1
    return ans

def subsets(a):
    queue=[]
    for item in a:
        queue.append([item])
    all_subset=[[]]
    all_subset.extend(queue)
    while queue:
        item = queue.pop(0)
        index = a.index(max(item))
        rest = a[index+1:]
        temp = make(item, rest)
        queue.extend(temp)
        all_subset.extend(temp)

    return all_subset

a= [1, 2, 3, 4, 5, 6,7,8,9,10]
print(subsets(a))
print(make([1, 2, 3, 4], [5]))
