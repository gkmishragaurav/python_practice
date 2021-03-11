# Write a function that takes an array of integers and return an array of length 2 
# representing the largest range of integers contained in that array. first number 
# of the o/p should be first number of range while 2nd number should be last number of range.


# time and space complexity is O(n)
def return_largest(a, mini, maxi):
    # a will be a dict.
    key = mini
    current=0
    largest=0
    range_=[None, None]
    largestRange_ = range_
    while key <= maxi:
        if key in a.keys():
            current = current+1
            if range_[0] == None:
                range_[0] = key
            else:
                range_[1] = key

            if current > largest:
                largest = current
                largestRange_ = range_

        else:
            current = 0
            range_=[None, None]

        key=key+1

    if not largestRange_[-1]:
        largestRange_[1] = largestRange_[0]

    return largestRange_

def largestRange(a):
    temp = {}
    i=0
    mini=float("inf")
    maxi=float("-inf")
    while(i<len(a)):
        if a[i] > maxi:
            maxi = a[i]

        if a[i] < mini:
            mini = a[i]

        temp[a[i]] = i
        i=i+1

    return return_largest(temp, mini, maxi)

a=[1] #[1,1]
# a = [2,3,4,5,6]
# a=[1, 11, 3, 0, 15, 5, 2, 4, 10, 7, 12, 6] # 0,7
print(largestRange(a))
