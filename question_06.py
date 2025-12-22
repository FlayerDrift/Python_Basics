"""
Problem 6: Best Time to Buy and Sell 
StockGoal: Given an array prices where prices[i] is the price of a given stock on the i^{th} day, find the maximum profit you can achieve. 
You may complete at most one transaction (buy one and sell one share of the stock).

Input: prices = [7, 1, 5, 3, 6, 4]
Output: 5 (Buy on day 2 (price=1) and sell on day 5 (price=6), profit = 6-1 = 5).

Strategy Hint (Sliding Window / Two Pointers):We want to minimize the buy price and maximize the profit.
Imagine two pointers:Left Pointer (buy_day): This is the day you decide to buy (the lowest price found so far).
Right Pointer (sell_day): This pointer scans every subsequent day (price).
If the price on sell_day is higher than buy_day, you calculate the profit and see if it's the new max profit.If the price on sell_day is lower than buy_day, 
the sell_day is now a better starting point. What should happen to the buy_day pointer in this case?
"""

prices = [7, 1, 5, 3, 6, 4]

def buy_sell(prices):
    low_price = prices[0]
    max_profit = 0

    for i in range(len(prices)):
        if low_price > prices[i]:
            low_price = prices[i]
        else:
            max_profit = max(max_profit, (prices[i]-low_price))

    print(max_profit)

buy_sell(prices=prices)