121. Best Time to Buy and Sell Stock
Solved
Easy
Topics
Companies
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
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





# Sliding window problem.
# Initialize two pointers, l and r, where l is the left pointer (buy day) and r is the right pointer (sell day).
# l = 0, r = 1
# Initialize maxProfit to 0 to keep track of the maximum profit.
# Iterate through the prices list with the right pointer.
# If the price at the right pointer is greater than or equal to the price at the left pointer,
# calculate the profit and update maxProfit if the calculated profit is greater.
# If the price at the right pointer is less than the price at the left pointer,
# move the left pointer to the right pointer.
# Always move the right pointer to the next day.
# Return the maximum profit after the loop ends.



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxProfit = 0
        while(r < len(prices)):
            if(prices[r] >= prices[l]):
                maxProfit = max(prices[r] - prices[l], maxProfit)
                #don't move l
            else:
                l=r #move l to r when you get a lesser value
            r+=1 #always increase r
        return maxProfit
