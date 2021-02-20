'''Given two non-empty arrays of integers, write a function that determines whether the second array is a subsequence of the first one.
A subsequence of an array is a set of numbers that aren't necessarily adjacent in the array but that are in the same order as they appear in the array.
For instance, the numbers [1, 3, 4] form a subsequence of the array [1, 2, 3, 4] , and so do the numbers [2, 4] .
Note that a single number in an array and the array itself are both valid subsequences of the array.
Repeat of numbers is possible.
'''

def all_indices(my_list, item, num):
    indices = [i for i, x in enumerate(my_list) if x == item and i >= num ]
    return indices

def find_(a, x, start, end):
    print(a[start:end], x)
    return True if x in a[start:end] else False

def isValidSubsequence(a, s):
    status=False
    start=0
    end=len(a)
    for x in s:
        if find_(a, x, start, end):
            status=True
            ai = all_indices(a, x, start)
            if ai:
                start=min(all_indices(a, x, start))+1
            else:
                status = False
                break
        else:
            status=False
            break
    return status

print(isValidSubsequence([5, 1, 22, 25, 6, -1, 8, 10],
                         [5, 1, 22, 25, 6, -1, 8, 10, 10]))
