# a number will be given in form of array, let say a = [1,2,3] for number 123
# a number can be single digit in array
# multiply a number to it in that array, let say m = 2, a*m = [2,4,6]
# form pascal traigle for row <= 5
def insert_at_start(a, x):
    if a:
        a.append(a[-1])
        i=len(a)-1
        while(i>0):
            a[i]=a[i-1]
            i=i-1
        a[0] = x

    return a

def multiply_in_array(a, m):
    # in a loop, start from last to first, multiply the number and keep the carry.
    n=len(a);i=n-1; carry=0
    while(i>=0):
        # pdb.set_trace()
        temp = (a[i] * m + carry) % 10
        carry = (a[i] * m + carry )/ 10
        a[i] = temp
        i=i-1

    # at last if there is a carry, insert it at the start
    if carry:
        while(carry):
            insert_at_start(a, carry%10)
            carry = carry/10

    return a

def pascal_traigle(row):
    i=0;a=[]
    while(i<row):
        if i == 0 :
            a=[1]
            print a
        else:
            print multiply_in_array(a, 11)
        i = i + 1

# a = [1]
# m = 11
#
# print multiply_in_array(a, m)

pascal_traigle(5)
