import pdb
def parent(a, i):
    return (i-1)/2

def left(a, i):
    return(2*i+1)

def right(a, i):
    return (2*i+2)

def swap(a,b):
    return b,a

def min_heapify(a, end=None):
    for i in range(end/2):
        left_child = left(a, i)
        right_child = right(a, i)
        if a[left_child] < a[i] and left_child < end:
            if a[right_child] < a[left_child]:
                a[i], a[right_child] = a[right_child], a[i]
            else:
                a[i], a[left_child] = a[left_child], a[i]
        if a[right_child] < a[i] and right_child < end:
            a[i], a[right_child] = a[right_child], a[i]
    return a

def max_heapify(a, end=None):
    for i in range(end/2):
        left_child = left(a, i)
        right_child = right(a, i)
        if a[left_child] > a[i] and left_child < end:
            if a[right_child] > a[left_child]:
                a[i], a[right_child] = a[right_child], a[i]
            else:
                a[i], a[left_child] = a[left_child], a[i]
        if a[right_child] > a[i] and right_child < end:
            a[i], a[right_child] = a[right_child], a[i]
    return a

def heap_sort(a):
    last = len(a)
    while(last):
        a = min_heapify(a, last)
        a[0], a[last-1] = a[last-1], a[0]
        last = last - 1
    return a

a = [3, 9, 2, 5, 6, 1, 8]
print a
print heap_sort(a)




