# A string consists of parenthesis and letters. validate if all the parenthesis are balanced.
# Ignore latters
# all three type of paranthesis are possible - '()', '[]', '{}','<>'
# Solution:
# One approach to check balanced parentheses is to use stack.
# Each time, when an open parentheses is encountered push it in the stack,
# and when closed parenthesis is encountered, match it with the top of stack
# and pop it. If stack is empty at the end, return Balanced otherwise, Unbalanced.

import pdb

open_para = ['(','{','[','<']
close_para = [')','}',']','>']
def balanced_paranthesis(s):
    stack=[]
    for i in range(len(s)):
        if s[i] in open_para:
            stack.append(s[i])
        elif s[i] in close_para:
            pos = close_para.index(s[i])
            if stack:
                temp = stack.pop()
                if temp == open_para[pos]: pass
            else:
                return 'Un-balanced'
    if stack:
        return 'Un-balanced'
    return 'Balanced'

s='<>[]{}()<><><><'
print balanced_paranthesis(s)