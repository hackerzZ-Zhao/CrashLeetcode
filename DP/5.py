class Solution:
    def longestPalindrome(self, s: str) -> str:
        # dp[i][j] represents whether the substring s[i:j] is palindrome
        # base cases would be dp[i][i] = True since we only have one character
        # since we need to decide whether a substring is palindrome or not and based on the definition of dp, we should traverse i for end to start and j for i + 1 to end.
        # only if s[i] == s[j] and dp[i + 1][j - 1] is palindrome, dp[i][j] = True
        # also we need to update the longest result
        n = len(s)
        res = ''
        dp = [[False for col in range(n)] for row in range(n)]
        for i in range(n):
            dp[i][i] = True
            res = s[i]
            
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                if s[i] == s[j]:
                    if j - i == 1 or dp[i + 1][j - 1]:
                        dp[i][j] = True
                        length = j - i + 1
                        if length > len(res):
                            res = s[i:j + 1]
                            
        return res
