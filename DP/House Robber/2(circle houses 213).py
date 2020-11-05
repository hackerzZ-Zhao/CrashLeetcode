Question:
You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given a list of non-negative integers nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example:
Input: nums = [2,3,2]
Output: 3
Explanation: You cannot rob house 1 (money = 2) and then rob house 3 (money = 2), because they are adjacent houses.

Solution:
class Solution:
    def rob(self, nums: List[int]) -> int:
        # Since the first house and the last house is adjancent and we want to rob as many houses as we can
        # So we need to consider two situations: not rob the first and not rob the last
        # if not rob the first house, we need to find the maximum profit in nums[1:]
        # if not rob the last house, we need to find the maximum profit in nums[:-1]
        # Top-down
        def dfs(houses, memo, start):
            if start >= len(houses):
                return 0
            if start in memo:
                return memo[start]
            
            profit = max(houses[start] + dfs(houses, memo, start + 2), dfs(houses, memo, start + 1))
            memo[start] = profit
            return profit
        
        memo1, memo2 = {}, {}
        if len(nums) == 1:
            return nums[0]
        
        return max(dfs(nums[1:], memo1, 0), dfs(nums[:-1], memo2, 0))
    
        # bottom-up
        # dp[i] means the maximum profit if we rob from house i
        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [0 for profit in range(n + 2)]
        dp2 = [0 for profit in range(n + 2)]
        # not rob first
        for i in range(n - 1, 0, -1):
            dp1[i] = max(nums[i] + dp1[i + 2], dp1[i + 1])  
        # not rob last
        for i in range(n - 2, -1, -1):
            dp2[i] = max(nums[i] + dp2[i + 2], dp2[i + 1])
            
        # Remeber the final result in dp1 is in dp1[1] since we only iterate [1:]
        return max(dp1[1], dp2[0])
            
        
        
        
