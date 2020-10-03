Problems:  
You are given coins of different denominations and a total amount of money amount.  
Write a function to compute the fewest number of coins that you need to make up that amount.  
If that amount of money cannot be made up by any combination of the coins, return -1.  

You may assume that you have an infinite number of each kind of coin.  

Example:
coins = [1,2,5], amount = 11, return 3

How to hack:
This is an entry level DP problem. Since we have infinite number of each coin, so we face the same situation even in the subproblems.  
For exmaple, if we want to come up a best solution amount of 11(like the solution above), we only need to know the best solution for amount of 10. 
Since we can directly add one to that answer to become our final answer (the minimum number of coins of 10 + 1（a one dollar coin） == the minimum number of coins of 11)

So according to this, we can set up a dp array which dp[i] means when the amount is i, the minimum number we need would be dp[i]
the base situation would be when the amount is 0, dp[0] == 0  
For each dp[i], we try each coin so that we can find the best solution. if i - coin >= 0, means we might have a better solution when we add one to dp[i - coin]

Solution: Python3

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[i] means when the amount is i, the minimum coins we need
        dp = [sys.maxsize] * (amount + 1)
        dp[0] = 0
        for i in range(len(dp)):
            for coin in coins:
                if i - coin >= 0:
                    dp[i] = min(dp[i], 1 + dp[i - coin])
                    
        return dp[amount] if dp[amount] != sys.maxsize else -1
