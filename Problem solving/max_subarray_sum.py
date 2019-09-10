# Max Sum Contiguous Subarray
# Write an efficient program to find the sum of contiguous subarray
# a one-dimensional array of numbers which has the largest sum.

def is_all_negetive(a):
    for i in range(len(a)):
        if a[i] > 0 :
            return False
    return True

def find_max(a):
    max=a[0];i=0
    while(i<len(a)):
        if a[i] > max:
            max=a[i]
        i=i+1

    return max

def max_subarray_sum(a):
    if not is_all_negetive(a):
        sum=a[0];i=1;max=a[0]
        while(i<len(a)):
            if sum + a[i] > 0:
                sum = sum + a[i]
                if max < sum:
                    max = sum
            else:
                sum=0
            i=i+1
        return max
    else:
        return find_max(a)


a=[ -163, -20 ]
# a=[-2]
print max_subarray_sum(a)