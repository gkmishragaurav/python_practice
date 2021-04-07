import random
def partition(a, low, high):
    '''This partition will pick last element as pivot element.'''
    i=low-1;j=low;pivot= a[high]
    while(j < high):
        if a[j] < pivot:
            i=i+1
            a[i], a[j] = a[j], a[i]
        j=j+1
    a[i+1], a[high] = a[high], a[i+1]
    print a, i+1, high
    return a, i+1

def random_partition(a, low, high):
    ''' Take a random number as pivot element'''
    r = random.randint(low, high)
    a[r], a[high] = a[high] , a[r]
    return partition(a, low, high)

def quick_sort(a, low, high, rand=True):
    '''One round of quick sort will make sure that pivot element is on its right place.
    it means, left side element will be less than pivot and right side will be more than pivot.'''
    if low < high:
        if rand:
            a, pivot = random_partition(a, low, high)
        else:
            a, pivot = partition(a, low, high)
        print a, pivot
        quick_sort(a, low, pivot-1)
        quick_sort(a, pivot+1, high)
    return a

a = [90,80,70,60,50,40,30,20,10]
print quick_sort(a, 0, len(a)-1)


