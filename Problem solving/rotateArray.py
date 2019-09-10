def rotateArray(a, b):
    ret = []
    for i in xrange(len(a)):
        if i+b < len(a):
            ret.append(a[i + b])
        else:
            ret.append(a[i+(b%len(a))-len(a)])
    return ret

a=[ 14, 5, 14, 34, 42, 63, 17, 25, 39, 61, 97, 55, 33, 96, 62, 32, 98, 77, 35 ]
b=56
print rotateArray(a,b)