# generate parenthesis.
# 1 <= n <= 8

def generateParenthesis(n):
    strs = ['()']
    final=[]
    if n == 1: return ['()']
    while(1):
        zero = strs.pop(0)
        if len(zero) == n*2: break
        j=0
        while(j<=len(zero)):
            temp = insert_(zero, j)
            if temp not in strs:
                strs.append(temp)
            if temp not in final and len(temp) == n*2:
                final.append(temp)
            j=j+1
    return final

def insert_(s, k):
    # insert () at kth position.
    return s[:k] + '()' + s[k:]

print(generateParenthesis(8))
