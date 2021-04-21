# reverse string, recursive way

def reverse_util(s, rev_st, current):
    if current < 0:
        return (rev_st)

    rev_st = rev_st + s[current]
    return reverse_util(s, rev_st, current-1)

def reverse(s):
    rev_st = reverse_util(s, '', current=len(s)-1 )
    return rev_st


s='qwertyui'
print(reverse(s))
