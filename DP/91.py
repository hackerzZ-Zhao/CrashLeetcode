Problem:
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26
Given a non-empty string containing only digits, determine the total number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.

Example:
Input: s = "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).

Solution:

class Solution:
    def numDecodings(self, s: str) -> int:
        # first thought is using dfs. This way is easy to understand and write. Each time we pick one number or two numers, if they can be formed as a valid number, we go dfs to do further
        # count the number of ways if we choose one number of two numbers respectivley
        # use memoization to reduce the time complexity
        
#         def dfs(sub, memo):
#             if not sub:
#                 return 1
#             if sub in memo:
#                 return memo[sub]
            
#             takeOne = takeTwo = 0
#             if 1 <= int(sub[0]) <= 9:
#                 takeOne = dfs(sub[1:], memo)
#             if 10 <= int(sub[:2]) <= 26:
#                 takeTwo = dfs(sub[2:], memo)
                
#             total = takeOne + takeTwo
#             memo[sub] = total
#             return total
            
#         return dfs(s, {})
    
        # second thought would be try to convert dfs to dp. 
        # when you understand how dfs works, it's easy to convert it
        # dp[i] means the number of ways of decoding in substring s[:i]
        n = len(s)
        dp = [0] * (n + 1)
        dp[0] = 1 
        for i in range(1, n + 1):
            if s[i - 1] != '0':
                dp[i] = dp[i - 1]
            if i >= 2 and 10 <= int(s[i - 2: i]) <= 26:
                dp[i] += dp[i - 2]
                
        return dp[n]
