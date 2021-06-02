# Given an array, print the Next Smaller Element (NSE) for every element. 
# The Smaller smaller Element for an element x is the first smaller element 
# on the right side of x in array. Elements for which no smaller element exist (on right side), 
# consider next smaller element as -1. 

def NextSmallerElement(a):
    stack=[]
    i=0
    while i<len(a):
        if stack:
            if stack[-1]<a[i]:
                stack.append(a[i])
            else:
                while stack and stack[-1]>a[i]:
                    temp=stack.pop()
                    print(temp, a[i])
                stack.append(a[i])

        else:
            stack.append(a[i])

        i=i+1
    for item in stack:
        print(item, None)

a=[73,74,75,71,69,72,76,70]
NextSmallerElement(a)
