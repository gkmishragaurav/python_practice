# Count the frequency of a character.
# good space and time complexity
# given string is sorted and un-sorted.
# # binary search
def binary_search(a, k):
    i=0;j=len(a)-1
    if a[i] == k:
        return 0
    else:
        while(1):
            mid = (i+j+1)/2
            if a[mid] == k:
                return mid
            if a[mid] < k:
                i = mid
            else:
                j=mid
            if mid == j:
                return 'Not Found!'

def lower_bound(a, k):
    lb = binary_search(a, k)
    if lb == 0: return 0
    else:
        while(a[lb] == k):
            lb=lb-1
            if lb >= 0: break
    return lb

def upper_bound(a, k):
    ub = binary_search(a, k)
    print ub, len(a)
    if ub == len(a)-1: return ub
    else:
        while(a[ub] == k):
            ub=ub+1
            if ub < len(a): break
    return ub

def count_frequency(a, k):
    ub = upper_bound(a, k)
    lb = lower_bound(a, k)
    return ub-lb

a = [1,2,3,4,5,6,7,9,9]
k=9
print count_frequency(a, k)