# Return all palindrome in a string
# Return largest palindrome in a string

pd = []

def largest_palindrome():
    max=0
    st = None
    i=0
    while(i<len(pd)):
        if len(pd[i]) > max:
            max = len(pd[i])
            st = pd[i]
        i=i+1

    return st

def palindrome(s, start, end):
    while(start >=0 and end <len(s)):
        if s[start] == s[end]:
            if start != end:
                pd.append(s[start:end+1])
            start=start-1
            end=end+1
        else:
            break

# s = 'cabbacxyzpqrstsrqppqrstsrqpzyxcabbac'
s = 'abb'
n = len(s)
for i in range(n):
    # for odd
    palindrome(s, i, i)
    # for even
    palindrome(s, i, i+1)

print pd
print largest_palindrome()