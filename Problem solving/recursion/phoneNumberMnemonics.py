# Given a string containing digits from 2-9 inclusive, return all possible 
# letter combinations that the number could represent. Return the answer in any order.

d={
    '1': ['1'],
    '2': ['a','b','c'],
    '3': ['d','e','f'],
    '4': ['g','h', 'i'],
    '5': ['j','k','l'],
    '6': ['m','n', 'o'],
    '7': ['p','q', 'r', 's'],
    '8': ['t','u','v'],
    '9': ['w','x','y','z'],
    '0': ['0']
}
def util(a,b):
    ans = []
    for item in a:
        for i in b:
            ans.append(item+i)

    return ans

def sol(s, pos, ans):
    if pos == len(s):
        return ans
    ans = util(ans, d[s[pos]])
    return sol(s, pos+1, ans)


s= "0123456789"
ans = d[s[0]]
x=sol(s, 1, d[s[0]])
print(x)
