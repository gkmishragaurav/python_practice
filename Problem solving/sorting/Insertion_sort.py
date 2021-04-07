# Basically insert in a sorted list.
# worst time complexity O(n^2)
# best time complexity O(n) -- need to modify folloing code for that.
# avg. case time complexity O(n^2)
# Worst case space complexity O(1)

def insertion_sort(a):
    for i in range(1, len(a)):
        current = a[i]
        j=i-1
        while(j>=0 and a[j] > current):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=current

# a=[4, 2, 7, 3, 9, 1, 12, 6, 13, 8, 10]
a=[12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
insertion_sort(a)
print(a)