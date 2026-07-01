"""
121. Best Time to Buy and Sell Stock
Easy

You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
day = 0 = i = index and prices[day] = prices[i] = 7
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.


Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
 

Constraints:

1 <= prices.length <= 105
0 <= prices[i] <= 104

"""

class Solution(object):
    def maxProfit(self, prices):
        max_profit = 0
        min_price = prices[0]
        length_of_prices = len(prices)
        
        for day in range(length_of_prices):
            profit = prices[day] - min_price

            min_price = min(min_price, prices[day])

            max_profit = max(max_profit, profit)

        return max_profit

    
prices_1 = [7,6,4,3,1]
prices_2 = [7,1,5,3,6,4]

print(Solution().maxProfit(prices_1))
print(Solution().maxProfit(prices_2))



# class Solution(object):
#     def __init__(self, prices):
#         self.prices = prices

#     def maxProfit(self):
#         """
#         :type prices: List[int]
#         :rtype: int
#         """
#         profits = []
#         lenght_of_prices = len(self.prices)
#         print(lenght_of_prices)
#         for day in range(lenght_of_prices):
#             future_day = day + 1
#             for future_day in range(lenght_of_prices):
#                 profit = self.prices[future_day] - self.prices[day]
#                 if profit > 0:
#                     profits.append(profit)
#         return max(profits)