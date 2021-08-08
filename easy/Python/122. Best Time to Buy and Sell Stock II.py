#Date:080821
#Question:

#You are given an array prices where prices[i] is the price of a given stock on the ith day.

#Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times).

#Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).


#Type: Easy


#Thoughts:

#No idea in the beginning... but after reading some discussion,
#eventually it's just add up numbers if the tomorrow's price is greater than today's
#so in the beginning define a variable of total profit
# then write a loop, since we're going to be using i+1, the loop will
#only go through length of prices -1, else it will be index error 


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                total_profit += (prices[i+1] - prices[i])
        return total_profit
            

#Runtime: 52 ms, faster than 97.50% of Python3 online submissions for Best Time to Buy and Sell Stock II.
#Memory Usage: 15.2 MB, less than 23.09% of Python3 online submissions for Best Time to Buy and Sell Stock II.
#08/08/2021 16:14	Accepted	52 ms	15.2 MB	python3
