# Basically insert in a sorted list.
# worst time complexity O(n^2)
# best time complexity O(n) -- need to modify folloing code for that.
# avg. case time complexity O(n^2)
# Worst case space complexity O(1)

def insertion_sort(a):
    for i in range(1, len(a)):
        j=i
        current=a[i]
        while(j>0 and a[j-1]>current):
            a[j] = a[j-1]
            j-=1
            print(a)
        a[j]=current

a=[4, 2, 7, 3, 9, 1, 12, 6, 13, 8, 10]
insertion_sort(a)
print(a)


