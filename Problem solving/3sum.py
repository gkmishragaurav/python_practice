# Write a function that takes a non-empty array and an integer representing a target sum. 
# That finction should find all triplets in the array that sum up to the target sum.

def threeSum(a):
    a.sort()
    i=0
    s=[]
    while i <= len(a)-2:
        j=i+1
        k=len(a)-1
        while k>j:
            temp=a[i]+a[j]+a[k]
            print(temp)
            if temp == 0:
                if (a[i], a[j], a[k]) not in s:
                    s.append((a[i], a[j], a[k]))
                j=j+1
                k=k-1
            elif temp > 0:
                k=k-1
            else:
                j=j+1
        i=i+1

    return s

a=[-1,0,1,2,-1,-4]
print(threeSum(a))
