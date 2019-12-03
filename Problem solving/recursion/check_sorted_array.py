# Given an array, check whether array is in sorted order with recursion.

def is_sorted(a):
    if len(a) == 1:
        return True
    else:
        if a[0] < a[1]:
            return is_sorted(a[1:])
        else:
            return False

a= [127, 220, 246, 277, 321, 454, 534, 565, 877]
print is_sorted(a)