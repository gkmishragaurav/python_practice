# Select the largest/smallest element and put it at its spot(last/first)
# worst time complexity O(n^2)
# best time complexity O(n^2) -- need to modify folloing code for that.
# avg. case time complexity O(n^2)
# Worst case space complexity O(1)

def find_max(a, start, end):
    max=a[0],0
    for i in range(start, end):
        if a[i] > max[0]:
            max=a[i], i

    return max

def selection_sort(a):
    for i in range(len(a)-1, 0, -1):
        max=find_max(a, 0, i)
        print(max, a)
        if a[max[1]] > a[i]:
            a[i], a[max[1]] = a[max[1]], a[i]


a=[4, 2, 7, 3, 9, 1, 12, 6, 13, 8, 10]
selection_sort(a)
print(a)