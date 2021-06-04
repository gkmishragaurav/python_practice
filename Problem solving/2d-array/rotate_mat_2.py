# Rotate Matrix Elements
# input
# a= [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
#     ]
# expected_output
# [
#   [7,4,1],
#   [8,5,2],
#   [9,6,3]
#   ]
def transpose(a):
    # swap(matrix[i][j], matrix[j][i])
    i=0
    while i<len(a):
        j=i+1
        while j<len(a[0]):
            print(i,j)
            a[i][j], a[j][i] = a[j][i], a[i][j]
            j=j+1
        i=i+1
    return a

def vertical_flip(a):
    i=0
    while i<len(a):
        l=0;r=len(a)-1
        while r>l:
            a[i][l], a[i][r] = a[i][r], a[i][l]
            l=l+1
            r=r-1

        i=i+1

    return a

def rotate_mat(a):
    return vertical_flip(transpose(a))

a = [
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
]

x=rotate_mat(a)
print(x)
