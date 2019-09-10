# s = "30[a]2[bc]", return "aaabcbc".
# s = "3[a2[c]]", return "accaccacc".
# s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

s = "10[abc]3[cd]ef"

import pdb
def decodeString(s):
    stack = []
    l = len(s)
    for i in range(l):
        if s[i] != ']':
            stack.append(s[i])
        else:
            st=''
            while(1):
                xx = stack.pop()
                if xx != '[':
                    st = st+xx
                else:
                    num=''
                    while(1):
                        try:
                            if stack:
                                if 48 <= ord(stack[-1]) <= 57:
                                    num = num + stack.pop()
                                else:
                                    break
                            else: break
                        except TypeError:
                            break

                    temp = st*int(num[::-1])
                    temp=temp[::-1]

                    stack.append(temp)
                    break

    return("".join(stack))

print decodeString(s)