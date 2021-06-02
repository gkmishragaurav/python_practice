# Given a circular array arr[] consisting of N integers,
# the task is to print the Next Greater Element for every element of the circular array.
# Elements for which no greater element exist, print “-1”.
# Examples:
# Input: arr[] = {5, 6, 7}
# Output: 6 7 -1


def nextGreaterElement(a):
    stack=[]
    i=0
    ans=[-1 for _ in a]
    while i<len(a):
        if stack:
            if stack[-1][0]>a[i]:
                stack.append([a[i],i])
            else:
                while stack and stack[-1][0]<a[i]:
                    temp, index=stack.pop()
                    print(temp, a[i])
                    ans[index] = a[i]
                stack.append([a[i],i])

        else:
            stack.append([a[i],i])

        i=i+1

    i=0
    while i<len(a) and stack:
        while stack[-1][0]<a[i]:
            temp, index=stack.pop()
            print(temp, a[i])
            ans[index] = a[i]
        i=i+1

    print(ans)

a=[2, 6, 7, 2, 2, 2]
nextGreaterElement(a)

