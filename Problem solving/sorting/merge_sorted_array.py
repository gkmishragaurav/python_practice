# merge two sorted array

def merge_array(a,b):
    i=0;j=0
    while j<len(b) and i<len(a):
        if b[j] > a[i]:
            i=i+1

        else:
            a.insert(i, b[j])
            j=j+1

    if j < len(b):
        a[len(a):] = b[j:len(b)]
        # a.extend(b[j:len(b)])
    return a

print(merge_array([5, 8, 9],
                  [4, 7, 8, 11, 34],))
