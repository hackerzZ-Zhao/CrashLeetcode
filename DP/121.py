class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # N = len(prices)
        # res = 0
        # minP, maxP = sys.maxsize, 0
        # for i in range(N):
        #     if minP > prices[i]:
        #         minP = prices[i]
        #         maxP = 0
        #     if maxP < prices[i]:
        #         maxP = prices[i]
        #     res = max(res, maxP - minP)
        # return res
        
        # dp[i][k][0] means the profit at day i, when we have k times transaction, and we don't have rest stock on hand(0)
        # dp[i][k][1] means the profit at at day i, when we have k times transaction, and we have rest stock on hand(1)
        # so dp[i][k][0] = max(no transaction, sell it)
        # = max(dp[i - 1][k][0], dp[i - 1][k - 1][1] + prices[i])
        # dp[i][k][1] = max(no transaction, buy it)
        # = max(dp[i - 1][k][1], dp[i - 1][k][0] - prices[i])
        # take care of k, only when finish buy and sell operations, k -= 1
        # here we let k -= 1 when buy it
        
        if not prices:
            return 0
        n = len(prices)
        dp = [[0 for col in range(2)] for row in range(n)]
        dp[0][0] = 0
        dp[0][1] = -prices[0]
        for i in range(1, n):
            # since k always equal to 1 so we dont need to set this k variable
            # dp[i][k][0] initally should be == max(dp[i - 1][k][0], dp[i - 1][k][1] + prices[i])
            # since k always == 1, we can ingore it
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # since we only allow buy once, so each time we compare -prices[i] and keep (dp[i - 1][1])
            dp[i][1] = max(dp[i - 1][1], -prices[i])
            
        return dp[n - 1][0]
        
