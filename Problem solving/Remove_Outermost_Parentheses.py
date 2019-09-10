#A valid parentheses string is either empty (""), "(" + A + ")", or A + B, where A and B are valid parentheses strings,
#and + represents string concatenation.  For example, "", "()", "(())()", and "(()(()))" are all valid parentheses strings.
#A valid parentheses string S is primitive if it is nonempty, and there does not exist a way to split it into S = A+B,
# with A and B nonempty valid parentheses strings.
#Given a valid parentheses string S, consider its primitive decomposition: S = P_1 + P_2 + ... + P_k,
# where P_i are primitive valid parentheses strings. Return S after removing the outermost parentheses of every
# primitive string in the primitive decomposition of S.

# Example 1:
# Input: "(()())(())"
# Output: "()()()"

# Example 2:
# Input: "(()())(())(()(()))"
# Output: "()()()()(())"

s="(()())(())"

def func(st):
    bal=0
    stack=[]
    res=''
    for x in st:
        if x=='(': bal=bal+1
        else: bal=bal-1
        stack.append(x)
        if bal==0:
            stack.pop(0)
            stack.pop(-1)
            res=res+''.join(stack)
            stack=[]

    return res

print func(s)