def binarySearch_iterative(array, start, end, target):
    # Write your code here.
    while(end >= start):
        mid = int(start+end/2)
        if target == array[mid]:
            return mid
        elif target < array[mid]:
            end = mid-1
        else:
            start = mid+1

    return -1

def binarySearch_recursive(array, start, end, target):
    # Write your code here.
    if end < start:
        return -1
    mid = int((start+end)/2)
    if target == array[mid]:
        return mid
    elif target < array[mid]:
        return binarySearch_recursive(array, start, mid-1, target)
    elif target > array[mid]:
        return binarySearch_recursive(array, mid+1, end, target)



a = [1, 5, 23, 111]
print(binarySearch_recursive(a, 0, len(a)-1, 33))

