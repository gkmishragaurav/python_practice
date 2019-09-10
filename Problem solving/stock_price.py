# a represent the list for stock price in time line.
# You need to find a pair with max profit.
# left element of pair will be buy price, right one will be selling price.
# 2nd element cant be in left of first element.

a = [10, 20, 3, 15, 1, 22, 30]
n=len(a)
i=0
j=1
diff=a[j]-a[i]
pair = [(a[i], a[j])]

while(j<n):
    if diff < a[j] - a[i]:
        # update diff and pair
        diff = a[j] - a[i]
        pair.pop()
        pair.append((a[i], a[j]))
    j=j+1
    if j<n:
        if a[j]<pair[0][0]:
            i=j
            j=j+1
print pair

def stock_price_rec(a, i=0, j=1, pair=(a[0],a[1]), diff=a[1]-a[0]):
    '''Recursive solution for stock price.'''
    if j==len(a):
        print pair
        return
    if a[j] < pair[1]:
        i=j
    if a[j]-a[i] > diff:
        pair = (a[j], a[i])
        diff = a[j] - a[i]
    stock_price_rec(a, i, j+1, pair, diff)

def stock_price(a):
    '''Iterative solution for stock price.'''
    i=0; j=2
    pair=(a[0],a[1])
    diff = a[1]-a[0]
    while(j<len(a)):
        if a[j] < pair[1]:
            i=j
        if a[j]-a[i] > diff:
            pair = (a[j], a[i])
            diff = a[j] - a[i]
        j=j+1
    return pair

print stock_price_rec(a)