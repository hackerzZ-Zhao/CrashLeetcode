Problem:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.


Example:
Input: s = ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()".
    
Solution:

class Solution:
    def longestValidParentheses(self, s: str) -> int:
#         stack
#         if '(', push. if ')', stack.pop(), if stack, means substring between i and stack.top() are valid. 
#         if not stack, means until i, the substring from start point is valid
        
#         res, start, n = 0, 0, len(s)
#         stack = []
#         for i in range(n):
#             if s[i] == '(':
#                 stack.append(i)
#             else:
#                 if not stack:
#                     start = i + 1
#                 else:
#                     stack.pop()
#                     res = max(res, i - start + 1) if not stack else max(res, i - stack[-1])
                    
#         return res
    
        # dp
        # dp[i] means the longest result ends at s[i]
        n = len(s)
        if n < 2:
            return 0
        
        # if we have '...()', dp[i] = dp[i - 2] + 2 which means dp['...'] + '()'
        # if we have '...))', the second last ')' will have its corresponding '(' at position i - dp[i - 1]
        # so if we have '(' at position i - dp[i - 1] - 1, it will become the pair of the last ')'
        # and we need to find dp[i - dp[i - 1] - 2] which can be connected to cur substring and become the longest result at dp[i]
        
        dp = [0] * n
        dp[1] = 2 if s[:2] == '()' else 0
        for i in range(2, n):
            if s[i] == ')' and s[i - 1] == '(':
                dp[i] = dp[i - 2] + 2
            elif s[i] == s[i - 1] == ')':
                if i - dp[i - 1] - 1 >= 0 and s[i - dp[i - 1] - 1] == '(':
                    pre = dp[i - dp[i - 1] - 2] if i - dp[i - 1] - 2 >= 0 else 0
                    dp[i] = pre + dp[i - 1] + 2
                    
        return max(dp)
        
