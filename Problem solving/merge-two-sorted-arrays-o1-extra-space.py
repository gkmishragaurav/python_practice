# Merge two sorted arrays with O(1) extra space
# https://www.geeksforgeeks.org/merge-two-sorted-arrays-o1-extra-space/

def insert_array(a, x, first=True):
    if first:
        a[0] = x
    else:
        a[-1] = x
    return (sorted(a))

def merge_array(a1, a2):

    while(a1[-1] > a2[0]):
        temp = a1[-1]
        a1 = insert_array(a1, a2[0], False)
        a2 = insert_array(a2, temp)
    return a1, a2

arr1 = [1, 5, 9, 10, 15, 20]
arr2 = [2, 3, 8, 13]

print merge_array(arr1, arr2)