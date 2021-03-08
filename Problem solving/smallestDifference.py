# Write a function that takes in two non-empty arrays of integers,
# finds the pair of numbers (one from each array) whose absolute difference is closest to zero,
# and returns an array containing these two numbers, with the number from the first array in the first position.

def smallestDifference(a,b):
    a.sort()
    b.sort()
    i=0;j=0;min_diff=abs(a[i]-b[j])
    pair=(a[i], b[j])
    while(i < len(a) and j < len(b)):
        diff = abs(b[j] - a[i])
        if diff == 0:
            return (a[i], b[j])
        elif diff < min_diff:
            pair=(a[i], b[j])
            min_diff = diff

        if a[i] < b[j] :i=i+1
        elif a[i] > b[j]: j=j+1

    return pair


a = [-1, 5, 10, 20, 28, 3]
b = [26, 134, 135, 15, 17]


print (smallestDifference(a, b))
