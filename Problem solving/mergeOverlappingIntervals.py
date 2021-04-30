# Given a set of time intervals in any order, merge all overlapping intervals into one and
# output the result which should have only mutually exclusive intervals. Let the intervals be
# represented as pairs of integers for simplicity.
# For example, let the given set of intervals be {{1,3}, {2,4}, {5,7}, {6,8}}.
# The intervals {1,3} and {2,4} overlap with each other, so they should be merged and become
# {1, 4}. Similarly, {5, 7} and {6, 8} should be merged and become {5, 8}

def is_overlapping(l1, l2):
    if not l1: return True
    if l1[1] >= l2[0]:
        return True
    return False

def mergeOverlappingIntervals(a):
    # Write your code here.
    a.sort(key= lambda item: item[0] )
    i=0
    ans=[]
    curr=[]
    while i<len(a):
        if is_overlapping(curr, a[i]):
            if not curr:
                curr=a[i]
            curr = [min(curr[0], a[i][0]), max(curr[1], a[i][1])]
        else:
            ans.append(curr)
            curr=a[i]

        if i == len(a)-1:
            ans.append(curr)

        i=i+1

    return ans

a =  [ [1, 22],
       [-20, 30]]

print(mergeOverlappingIntervals(a))
