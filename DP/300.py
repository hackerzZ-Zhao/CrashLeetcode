Problems:  
Given an unsorted array of integers, find the length of longest increasing subsequence.

Examples:
nums = [10,9,2,5,3,7,101,18], return 4

How to hack:
difference between subsequence and substring:  
   subsequence not requires the element should be continuous while substring does. But you have to keep the original order.

Let's find the subproblems first:
nums = [], return 0
nums = [10], return 1
nums = [10, 9], return 1 (cannot change the origianl order)
nums = [10, 9, 2], return 1
nums = [10, 9, 2, 5], return 2 since [2, 5]
nums = [10, 9, 2, 5, 3], return 2 since [2, 5] or [2, 3]
nums = [10, 9, 2, 5, 3, 7], return 3 since [2, 3, 7] or [2, 5, 7]
....

Find out that 7 can be added after 5 or 3 and become a new subsequence. 
In other words, if we know the longest result of the previous subarray ended at nums[i - 1], we can find out the answer for the next subarray ended at nums[i]
by comparing each element j before nums[i], if nums[i] > j, means we can add nums[i] after the answer k of subarray nums[:j], so the tempoary answer would be k + 1.  
and we compared all the tempoary answers and take the biggest one.

So we define dp[i] equals to the length of longest increasing subsequence ended by nums[i]. For example, dp[4] = 2, dp[5] = 3

Solution: Python3

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
                    
        return max(dp)
