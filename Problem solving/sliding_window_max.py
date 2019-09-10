# #
# Sliding Window Maximum (Maximum of all subarrays of size k)
#
# Given an array and an integer k, find the maximum for each and every contiguous subarray of size k.

def find_max(a, start, end):
    i=start;max=0
    while(i<=end):
        if max < a[i]:
            max = a[i]
        i=i+1

    return max

def sliding_window_max(a, k):
    # # find max for first k elements.
    max = find_max(a, 0, k-1)
    print max,
    start=0;end=k-1

    # remove 1 element, add another, do this till n
    while(1):
        start=start+1; end=end+1
        if end >= len(a):
            break
        else:
            if a[start-1] != max:
                if a[end] < max :
                    pass
                else:
                    max = a[end]
            else:
                max = find_max(a, start, end)
            print max,

     # # two case, repeat allowed or not, if yes keep count of max element.
    # pass

# a = [1,2,3,4,5,6,7]
# a = [7,6,5,4,3,2,1]
# a = [6,7,4,5,2,3,1]

k=3
sliding_window_max(a, k)