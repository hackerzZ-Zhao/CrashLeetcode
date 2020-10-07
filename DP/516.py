Problem:
Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example:
"bbbab" return 4 since 'bbbb'

how to hack:
In general, when the question combines the best values and subsequence, you have to think dp to satisfied the time complexity requirement.

Here we define dp[i][j] represent the longest subsequence in s[i:j + 1], then we consider how the status transfer:
The next status should dp[i - 1][j + 1], so the i loop should start from the end. There are two situations we would face with:
1. s[i] == s[j], so they can add to the result of dp[i + 1][j - 1] to become a longer subsequence. 
2. s[i] != s[j], this time we have to choose a better one from dp[i + 1][j] and dp[i][j - 1] since we cannot add both of them, we can only choose one side to add

In conclusion, this is how dp works:
if s[i] == s[j]:
  dp[i][j] = dp[i + 1][j - 1] + 2 # we add s[i] and s[j] to dp[i + 1][j - 1]
else:
  dp[i][j] = max(dp[i + 1][j], dp[i][j - 1]) # we choose a longer one
  
Finally, dp[0][n - 1] would be the answer
  
Solution:

  class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:  
        # dp[i][j] represents the longest subsequence in s[i: j + 1] 
        n = len(s)
        dp = [[0 for col in range(n)] for row in range(n)]
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])
                    
        return dp[0][n - 1]
