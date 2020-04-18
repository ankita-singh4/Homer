def max2profit(prices):
    # to find the maximum profit in an array when consecutive buying is allowed
    maxProfit = 0
    for i in range(1, len(prices)):
        if prices[i] > prices[i-1]:
            maxProfit += prices[i] - prices[i-1]
    return maxProfit


print(max2profit([7,6,4,3,1]))