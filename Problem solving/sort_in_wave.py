#
# Sort an array in wave form
#
# Given [1, 2, 3, 4]
#
# One possible answer : [2, 1, 4, 3]
# Another possible answer : [4, 1, 3, 2]
#
#     NOTE : If there are multiple answers possible, return the one thats lexicographically smallest.
#     So, in example case, you will return [2, 1, 4, 3]

def sort_in_wave(a):
    i=0
    a = sorted(a)
    while(i<len(a)-1):
        if i%2 == 0:
            if a[i] < a[i+1]:
                a[i] , a[i+1] = a[i+1], a[i]
        else:
            if a[i] < a[i+1]:
                a[i] , a[i+1] = a[i+1], a[i]

        i=i+2
    return a

a=[ 5, 1, 3, 2, 4 ]

# a = [1,2,3,4,5,6,7]
sort_in_wave(a)