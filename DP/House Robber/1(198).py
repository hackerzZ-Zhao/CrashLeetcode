Question:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security system connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers representing the amount of money of each house, determine the maximum amount of money you can rob tonight without alerting the police.

Example:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
             Total amount you can rob = 2 + 9 + 1 = 12.
             
Solution:
class Solution:
    def rob(self, nums: List[int]) -> int:
        # top-down
        # each house we can choose rob or not rob. If rob i house, we need to move i + 2 house for next consideration, if not rob, we move to i + 1 house to consider
        def dfs(nums, memo, start):
            if start >= len(nums):
                return 0
            if start in memo:
                return memo[start]
            
            profit = max(nums[start] + dfs(nums, memo, start + 2), dfs(nums, memo, start + 1))
            memo[start] = profit
            return profit
        
        memo = {}
        return dfs(nums, memo, 0)
    
        # bottom up
        # dp[i] means the maximum profit if we rob from i house
        # so dp[n] = 0 since we don't have house to rob(n >= len(nums))
        # it equals to we append two house with 0 money to the nums aray (nums -> nums + [0, 0])
        n = len(nums)
        dp = [0 for profit in range(n + 2)]
        for i in range(n - 1, -1, -1):
            dp[i] = max(dp[i + 1], nums[i] + dp[i + 2])
            
        return dp[0]
        
