def left(a, i):
    return(2*i+1)

def right(a, i):
    return (2*i+2)

def max_heapify(a, end=None):
    i=int(end/2)
    while i>=0:
        left_child = left(i)
        right_child = right(i)
        if left_child < end and a[left_child] > a[i] :
            if right_child < end and a[right_child] > a[left_child]:
                a[i], a[right_child] = a[right_child], a[i]
            else:
                a[i], a[left_child] = a[left_child], a[i]

        elif right_child < end and a[right_child] > a[i]:
            a[i], a[right_child] = a[right_child], a[i]

        i=i-1

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
