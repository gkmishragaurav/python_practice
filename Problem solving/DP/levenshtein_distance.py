def levenshtein_distance_2(a, b):
    m,n = len(a), len(b)
    d = [[0 for x in range(n + 1)] for y in range(m + 1)]

    for i in range(1, m + 1):
        d[i][0] = i
    for j in range(1, n + 1):
        d[0][j] = j

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if a[i - 1] == b[j - 1]:
                cost = 0
            else:
                cost = 1

            d[i][j] = min(d[i - 1][j] + 1,
                          d[i][j - 1] + 1,
                          d[i - 1][j - 1] + cost)

    return d[m][n]

def levenshtein_distance(a, b):
    # case 1
    if not a or not b:
        return max(len(a), len(b))

    # case 2
    if a[0] == b[0]:
        return sol(a[1:], b[1:])

    # case 3
    else:
        return 1 + min(
            sol(b[0]+a, b),
            sol(a[1:], b),
            sol(b[0]+a[1:], b)
        )


a = "abcdefghij"
b = "1234567890"
x=levenshtein_distance(a,b)
print(x)
