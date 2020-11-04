Question:
Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete at most two transactions.

Note: You may not engage in multiple transactions at the same time (i.e., you must sell the stock before you buy again).

Example:
Input: prices = [3,3,5,0,0,3,1,4]
Output: 6
Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.

Solution:
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Here we need to consider k so dp[i][k][0 | 1] means the maximum profit at day i, when we allow k times transations, currently hold(1) or not hold(0)
        # we reduce the time of transations when we buy it
        if not prices:
            return 0
        
        n = len(prices)
        dp = [[[0 for _ in range(2)] for k in range(3)] for row in range(n)]
        dp[0][2][0] = 0
        dp[0][2][1] = -prices[0]
        dp[0][1][0] = 0
        dp[0][1][1] = -prices[0]
        for i in range(1, n):
            dp[i][2][0] = max(dp[i - 1][2][0], dp[i - 1][2][1] + prices[i])
            # we use dp[i - 1][1][0] - prices[i] since we count transaction time when we buy it
            dp[i][2][1] = max(dp[i - 1][2][1], dp[i - 1][1][0] - prices[i])
            dp[i][1][0] = max(dp[i - 1][1][0], dp[i - 1][1][1] + prices[i])
            # we use dp[i - 1][0][0] - prices[i] since we count transaction time when we buy it
            # and dp[i - 1][0][0] == 0 so we only left -prices[i]
            dp[i][1][1] = max(dp[i - 1][1][1], -prices[i])
            
        return dp[n - 1][2][0]
        
