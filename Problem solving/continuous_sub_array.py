# Find out the maximum sub-array of non negative numbers from an array.
# The sub-array should be continuous. That is, a sub-array created by choosing the second and fourth element and skipping the third element is invalid.
# Maximum sub-array is defined in terms of the sum of the elements in the sub-array. Sub-array A is greater than sub-array B if sum(A) > sum(B).
# Example:
# A : [1, 2, 5, -7, 2, 3]
# The two sub-arrays are [1, 2, 5] [2, 3].
# The answer is [1, 2, 5] as its sum is larger than [2, 3]

def continuous_sub_array(a):
    i=0;start=0;end=0;pair=[start, end];sum=0;max=0
    while(i<len(a)):
        # increase till a -ve
        # keep the sum all along
        # keep start and stop as well
        if a[i] >= 0:
            if i>=1 and a[i-1] <0:
                start = i
            end=i
            sum=sum+a[i]
            print sum, max
            if max < sum:
                pair=[start, end]
                max=sum
        else:
            sum=0
            start=i
        i=i+1

    return a[pair[0]:pair[1]+1]

a = [ -1, 2, -5, -7, -2, 5 ]
print continuous_sub_array(a)
