# You are given an array prices where prices[i] is the price of a given stock on the ith day.
# Find the maximum profit you can achieve. You may complete as many transactions as you like
# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.

def maxProfit(prices):
    # return sum([max(prices[i]-prices[i-1], 0) for i in range(1, len(prices))])
    i=0
    start, end = 0, None
    temp = []
    max_sum=0
    while i<len(prices)-1:
        if prices[i] < prices[i+1]:
            end = i+1
        else:
            if end:
                temp.append((start, end))
                max_sum=max_sum+(prices[end]-prices[start])
            start=i+1

        i=i+1

    return (temp, max_sum)

print(maxProfit([7,1,5,3,6,4]))
