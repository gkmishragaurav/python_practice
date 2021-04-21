# Questions on pointers and a long list was given comprising of binaries 0/1 in random order.
# The task was to achieve longest possible alternating sequence possible without using extra space.

def longest_alternate(s):
    start, end = 0, None
    i=0
    current=s[start]
    count=0
    max_diff = float('-inf')
    while i<len(s):
        if s[i] == current:
            end=i
            if end-start > max_diff:
                max_diff = end-start
            count=count+1
            current='0' if current=='1' else '1'

        else:
            start=i
            count=0

        i=i+1

    return max_diff+1

# 0101010101
print(longest_alternate('00010101010111111100000'))
