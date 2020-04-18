def maxProfit(prices):
    # find the maximum profit while buying and selling shares
    maximumP = 0
    minPrices = 10000
    for p in prices:
        if p < minPrices:
            minPrices = p
        elif p - minPrices > maximumP:
            maximumP = p - minPrices
    return maximumP



print(maxProfit([7,6,4,3,1]))

