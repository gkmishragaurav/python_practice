# There are N children standing in a line with some rating value.
# You want to distribute minimum number of candies to these children such that
# each child must have at least one candy and the children with higher
# rating will have more candies than his neighbour.
# Write a program to calculate the minimum candies you must give.
# https://afteracademy.com/problems/distribute-candy-problem

def candy(a):
    ans = [1 for _ in a]
    # forward check
    i=0
    while i<len(a)-1:
        if a[i] > a[i+1]:
            ans[i]=max(2, ans[i])
            ans[i+1]=1
        elif a[i] == a[i+1]:
            ans[i+1] = 1
        else:
            if not ans[i]:
                ans[i]=ans[i]+1
            ans[i+1]=ans[i]+1
        i=i+1

    # backward check
    i=len(a)-1
    while i>0:
        if a[i] < a[i-1]:
            if ans[i] < ans[i-1]:
                pass
            else:
                ans[i-1] = ans[i]+1
        i=i-1

    print(ans)
    return sum(ans)

a=[2,3,4,4,3,2,1]
print(candy(a))
