# Step 1 − Initialize the value of h
# Step 2 − Divide the list into smaller sub-list of equal interval h
# Step 3 − Sort these sub-lists using insertion sort
# Step 3 − Repeat until complete list is sorted

def gap_insertion_sort(a, start, gap):
    '''This will be insertion sort based, but gap based'''
    for i in range(start, len(a), gap):
        current = a[i]
        j=i-1
        while(j>=0 and a[j] > current):
            a[j+1]=a[j]
            j=j-1
        a[j+1]=current

def shell_sort(a):
    gap=int(len(a)/2)
    while(gap>=1):
        for start in range(gap):
            gap_insertion_sort(a, start, gap)
        gap=int(gap/2)

a=[4, 2, 7, 3, 9, 1, 12, 6, 13, 8, 10]
shell_sort(a)
print(a)