# Given an integer k, return the minimum number of Fibonacci numbers whose sum is equal to k.
# The same Fibonacci number can be used multiple times.
# The Fibonacci numbers are defined as:
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2 for n > 2.
# It is guaranteed that for the given constraints we can always find such Fibonacci numbers that sum up to k.
# Example 1:
# Input: k = 7
# Output: 2 
# Explanation: The Fibonacci numbers are: 1, 1, 2, 3, 5, 8, 13, ... 
# For k = 7 we can use 2 + 5 = 7.
# # 1 <= k <= 10^9

def get_fib_list(k):
    temp=[1,1]
    i=2
    while i<=k:
        x=temp[-1]+temp[-2]
        if x<=k:
            temp.append(x)
        else:
            break

        i=i+1

    return temp

def findMinFibonacciNumbers(k):
    temp = get_fib_list(k)
    print(temp)
    i=len(temp)-1
    s=[]
    while i>=0:
        s.append(temp[i])
        if sum(s) == k:
            return len(s)
        elif sum(s) > k:
            s.pop()
        i=i-1


x=findMinFibonacciNumbers(99999)
print(x)

