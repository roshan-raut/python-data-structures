"""
Your task is to return the maximum profit from the function buy_and_sell_stock_once(prices) given in the code widget
below. The input parameter prices is the array of integers that​
contains the price of stocks at each day where a day is represented by the index.

Note that you need to buy the stocks before you sell them so the day (index) indicating the buying price
should be before the day (index) indicating the selling price.
"""


def buy_and_sell_stock_once(prices):
    max_profit = []
    i = 0
    for i in range(len(prices)):
        # j = i+1
        for j in range(i+1, len(prices)):
            if prices[j] > prices[i]:
                profit = prices[j] - prices[i]
                max_profit.append(profit)
            j += 1
        i += 1
    max_profit = sorted(max_profit)
    if len(max_profit) > 1:
        return max_profit.pop()
    return 0

# Time Complexity: O(n^2)
# Space Complexity: O(1)
def buy_and_sell_once(prices):
    max_profit = 0
    for i in range(len(prices)-1):
        for j in range(i+1, len(prices)):
            if prices[j] - prices[i] > max_profit:
                max_profit = prices[j] - prices[i]
    return max_profit


'''
In solution 2, for each index, we calculate the most profit we can make by selling at that time. 
So, for a given day, the maximum profit can be made if the stock were bought at the minimum price on an earlier day. 
Therefore, we maintain the minimum price seen so far and subtract it from every future price 
to keep track of the maximum profit.

We iterate the array once and keep track of the minimum buying price and the maximum profit. 
We calculate the profit at each iteration by subtracting the minimum buying price seen so far from the current price 
in each iteration and updating the maximum profit accordingly.
'''
# Time Complexity: O(n)
# Space Complexity: O(1)
def buy_and_sell_once1(prices):
    max_profit = 0.0
    min_price = float('inf')
    for price in prices:
        min_price = min(min_price, price)
        compare_profit = price - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit


# print(buy_and_sell_stock_once([50, 40, 30, 20, 10]))
# print(buy_and_sell_once([100, 180, 260, 310, 40, 535, 695]))
print(buy_and_sell_once1([310, 315, 275, 295, 260, 270, 290, 230, 255, 250]))