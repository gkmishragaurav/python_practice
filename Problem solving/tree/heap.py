def left(i):
    return 2 * i + 1


def right(i):
    return 2 * i + 2


def max_heapfy(a, start, end, limit):
    i = end
    while i >= start:
        l = left(i)
        r = right(i)
        l = a[l] if l <= limit else None
        r = a[r] if r <= limit else None
        max_tuple = [a[i]]
        if l: max_tuple.append(l)
        if r: max_tuple.append(r)
        if max(max_tuple) != a[i]:
            if l and r:
                if r > l:
                    a[i], a[right(i)] = a[right(i)], a[i]

                else:
                    a[i], a[left(i)] = a[left(i)], a[i]
            elif l:
                a[i], a[left(i)] = a[left(i)], a[i]

            elif r:
                a[i], a[right(i)] = a[right(i)], a[i]

        i = i - 1

    return a

a = [3, 8, 2, 5, 6, 1, 9]

def heap_sort(a):
    last = len(a)
    while last:
        max_heapfy(a, 0, int(last/2)-1, last-1)
        a[0], a[last-1] = a[last-1], a[0]
        last=last-1

heap_sort(a)
print(a)
