Question:
You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

Design an algorithm to find the maximum profit. You may complete at most k transactions.

Notice that you may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

Example:
Input: k = 2, prices = [2,4,1]
Output: 2
Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.

Solution:
class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        def maxProfit_inf(prices):
            # k = infinity
            # based on 121, we don't need to record k
            n = len(prices)
            dp = [[0 for col in range(2)] for row in range(n)]
            dp[0][0] = 0
            dp[0][1] = -prices[0]
            for i in range(1, n):
                dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
                dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

            return dp[n - 1][0]
        
        if not prices:
            return 0
        
        n = len(prices)
        # buy and sell at least need two days, so if k > half of days(len(prcies) // 2), this problem is same as problem 122
        if n // 2 < k:
            return maxProfit_inf(prices)
        
        # Otherwise we do the same algorithm as problem 123
        dp = [[[0 for status in range(2)] for times in range(k + 1)] for day in range(n)]
        for t in range(1, k + 1):
            dp[0][t][0] = 0
            dp[0][t][1] = -prices[0]
            
        for i in range(1, n):
            for t in range(k, 0, -1):
                dp[i][t][0] = max(dp[i - 1][t][0], dp[i - 1][t][1] + prices[i])
                dp[i][t][1] = max(dp[i - 1][t][1], dp[i - 1][t - 1][0] - prices[i])
                
        return dp[n - 1][k][0]
