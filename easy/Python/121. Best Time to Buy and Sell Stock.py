#Date:080821
#Question:

#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

#Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.


#Type: Easy


#Thoughts:

#first, define a variable of max profit and min price,
# and go through the loop, use max and min built in function
# compare the max profit value with price[i]-min price, update if it's greater than max profit
#and also check the min price
#return max profit.



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
     
        max_profit = 0
        min_price = prices[0]
        
        for i in range(1, len(prices)):
            max_profit = max(max_profit, prices[i]-min_price)
            min_price = min(min_price, prices[i])
        
        return max_profit

#Runtime: 1128 ms, faster than 25.88% of Python3 online submissions for Best Time to Buy and Sell Stock.
#Memory Usage: 25.2 MB, less than 53.15% of Python3 online submissions for Best Time to Buy and Sell Stock.
#08/08/2021 15:29	Accepted	1128 ms	25.2 MB	python3
        
