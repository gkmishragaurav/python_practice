def insert_carry(s, carry):
    while(carry):
        s.insert(0, carry%10)
        carry=carry/10

def multiply(s, k):
    i=len(s)-1
    carry=0
    while(1):
        d = (s[i]*k+carry)/10
        s[i] = (s[i]*k+carry)%10
        carry = d
        i=i-1
        if i<0:
            if carry != 0:
                insert_carry(s, carry)
            break
    return s

def num_to_arr(n):
    arr=[]
    while(n):
        arr.insert(0, n%10)
        n=n/10
    return arr

def arr_to_str(arr):
    st = ''
    for x in arr:
        st=st+str(x)

    return st

def extraLongFactorials(n):
    if n==0:
        arr=[1]
    else:
        arr = num_to_arr(n)
        n=n-1
        while(n):
            arr = multiply(arr, n)
            n=n-1
    print arr_to_str(arr)
    return

n=1000
extraLongFactorials(n)