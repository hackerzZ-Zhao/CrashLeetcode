Question:
Given a string s, find the length of the longest substring without repeating characters.

Example:
Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Solution:
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Sliding window
        # We use a set to record the letter we met and move the right pointer until it points to the letter already in the set, each move we update the length to res
        # Then we move left pointer until s[right] not in the set
        # If right pointer points to the end, we end it and return res
        visited = set()
        left, right = 0, 0
        n = len(s)
        res = 0
        
        while right < n:
            if s[right] not in visited:
                visited.add(s[right])
                right += 1
                res = max(res, right - left)
            else:
                while s[right] in visited:
                    visited.remove(s[left])
                    left += 1
                    
        return res
                    
                
                    
                
        
        
