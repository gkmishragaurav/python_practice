# Special Positions in a Binary Matrix
# Given a rows x cols matrix mat, where mat[i][j] is either 0 or 1,
# return the number of special positions in mat.
# A position (i,j) is called special if mat[i][j] == 1
# and all other elements in row i and column j are 0 (rows and columns are 0-indexed).
# Input: mat = [[1,0,0],
#               [0,0,1],
#               [1,0,0]]
# Output: 1
# Explanation: (1,2) is a special position because mat[1][2] == 1 and all other elements in row 1 and column 2 are 0.


def numSpecial(mat):
    sum_row = []
    sum_col = []

    # making sum_row
    for i in range(0,len(mat)):
        sum_row.append(sum(mat[i]))
    print(sum_row)

    # making sum_col
    for col in range(0, len(mat[0])):
        s=0
        for row in range(0, len(mat)):
            s=s+mat[row][col]
        sum_col.append(s)
    print(sum_col)

    count=0
    for row in range(0, len(mat)):
        for col in range(0, len(mat[0])):
            if mat[row][col] == 1 and sum_col[col]==1 and sum_row[row] == 1:
                count=count+1

    return count

mat = [[0,0,0,1],
       [1,0,0,0],
       [0,1,1,0],
       [0,0,0,0]]

print(numSpecial(mat))
