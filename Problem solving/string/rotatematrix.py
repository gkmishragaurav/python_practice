# Rotate Matrix Elements
# input
# a= [
#     [1, 2, 3],
#     [4, 5, 6],
#     [7, 8, 9]
# ]
# expected_output
# [
#     [4, 1, 2],
#     [7, 5, 3],
#     [8, 9, 6]
# ]

def shift_row_clock(a, row, start, end):
    # this will return temp as extra value to return in next cycle
    temp = None
    i=start
    while i <= end:
        temp, a[row][i] = a[row][i], temp
        i=i+1

    return temp

def shift_row_anti_clock(a, row, temp, start, end):
    # this will return temp as extra value to return in next cycle
    i = start
    while i >= end:
        temp, a[row][i] = a[row][i], temp
        i=i-1

    return temp

def shift_col_clock(a, col, temp, start, end):
    # this will return temp as extra value to return in next cycle
    i=start
    while i <= end:
        temp, a[i][col] = a[i][col], temp
        i=i+1

    return temp

def shift_col_anti_clock(a, col, temp, start, end):
    # this will return temp as extra value to return in next cycle
    i=start
    while i >= end:
        temp, a[i][col] = a[i][col], temp
        i=i-1

    return temp

def rotate_mat(a):
    colomn=len(a)-1
    row=0
    while row < colomn:
        # shift top row
        temp = shift_row_clock(a, row, start=row, end=colomn)
        print(temp, a)
        # shift last colomn
        temp = shift_col_clock(a, colomn, temp, start=row+1, end=colomn)
        print(temp, a)
        # shift last row
        temp = shift_row_anti_clock(a, len(a)-row-1, temp, start=colomn-1, end=row)
        print(temp, a)
        # shift first colomn
        temp = shift_col_anti_clock(a, len(a)-colomn-1, temp, start=colomn-1, end=row)
        print(temp, a)
        row=row+1
        colomn = colomn - 1


a = [
    [1, 2, 3, 10, 17],
    [4, 5, 6, 11, 18],
    [7, 8, 9, 12, 19],
    [13, 14, 15, 16, 20],
    [21, 22, 23, 24, 25]
]

rotate_mat(a)



