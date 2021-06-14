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
