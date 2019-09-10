# @param a : list of integers
# @return - add 1 to about number entered as list.
# this code will add x element at start of array, if 0s were in start then they will be skipped
# just before the first number, X will be added.
def insert_at_start(a, x):
    if a:
        a.append(a[-1])
        i=len(a)-1
        while(i>0):
            a[i]=a[i-1]
            i=i-1
        a[0] = x
    else:
        a.append(x)
    return a

def plusOne(a):
    if not a:
        a.append(1)
        return a
    # remove all 0 at are at start of array.
    i = 0
    while (i < len(a)):
        if a[i] == 0:
            del a[0]
            i = 0
        else:
            break
    n = len(a)
    # Add 1 to last digit and find carry
    a[-1] = a[-1]+1
    carry = a[-1]/10
    a[-1] = a[-1] % 10

    # Traverse from second last digit and settle carry till it is not 0
    if carry:
        i=n-2
        while(i>=0 and carry):
            a[i] = a[i] + carry
            carry = a[i] / 10
            a[i] = a[i] % 10
            i=i-1

    # If carry is 1, we need to add
    # this 1 need to be added at start of array
    if carry:
        insert_at_start(a, carry)

    return a


a = []

print plusOne(a)
