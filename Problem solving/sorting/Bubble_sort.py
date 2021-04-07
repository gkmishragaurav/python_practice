# Bubble sort or sinking sort.
# compare each pair of the list ans sort it if not in order.
# worst time complexity O(n^2)
# best time complexity O(n) -- need to modify folloing code for that.
# avg. case time complexity O(n^2)
# Worst case space complexity O(1)

def bubble_sort(a):
    for i in range(len(a)):
        for j in range(i, len(a)):
            if a[j]<a[i]:
                a[i],a[j] = a[j],a[i]

            print(a)

a=[4, 2, 7, 3, 9, 1, 12, 6, 13, 8, 10]
bubble_sort(a)
print(a)