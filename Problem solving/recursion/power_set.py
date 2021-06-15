# Power Set Power set P(S) of a set S is the set of all subsets of S. 
# For example S = {a, b, c} then P(s) = {{}, {a}, {b}, {c}, {a,b}, {a, c}, {b, c}, {a, b, c}}.
def sol(a, n, s):
    if tuple(s) not in d:
        d[tuple(s)] = 1

    if not a or n<0:
        return

    s.append(a[n])
    sol(a, n-1, s)
    s.pop()
    sol(a, n-1, s)


d={}
a = [1,2,3]
sol(a, len(a)-1, [])
print(d)
x = [list(k) for k,v in d.items()]
print(x)
