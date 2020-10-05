Problem:
Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

Insert a character
Delete a character
Replace a character

Examples:
Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

How to hack:
It's not easy to figure out how to hack at the first time. But actually the solution is not complex and this is an useful problem.
First, we need to transfer from word1 to word2, which means eventually we need each character in word1 is the same as word2
Second，we have three ways to make each character equal. Which one is the best? just try them all.
Brute force is not acceptable since there are too many duplicate situation will waste time.

Define dp[i][j] as the minimum operation make s1[:i] equal to s2[:j], base case is dp[0][j] = j and dp[i][0] = i
Then we translate our operation into code:
insert: insert a s2[j] at s1[i], then s1[i] match, move j
delelte: delete s1[i], move i to next and compare with s2[j]
replace: after replace s1[i] == s2[j], so move i and j

Solution:
class Solution:
    def minDistance(self, s1: str, s2: str) -> int:
        # dp[i][j] shows the minimum distance of s[:i] and s[:j]
        n1, n2 = len(s1), len(s2)
        dp = [[sys.maxsize for col in range(n2 + 1)] for row in range(n1 + 1)]
        for i in range(n1 + 1):
            dp[i][0] = i
            
        for i in range(n2 + 1):
            dp[0][i] = i
            
        
        for i in range(1, n1 + 1):
            for j in range(1, n2 + 1):
                if s1[i - 1] == s2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    insert = min(dp[i][j], dp[i][j - 1] + 1) 
                    delete = min(dp[i][j], dp[i - 1][j] + 1)
                    replace = min(dp[i][j], dp[i - 1][j - 1] + 1)
                    dp[i][j] = min(insert, min(delete, replace))
                    
        return dp[n1][n2]
