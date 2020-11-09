Question:
Given two strings s and t, return the minimum window in s which will contain all the characters in t. If there is no such window in s that covers all characters in t, return the empty string "".

Note that If there is such a window, it is guaranteed that there will always be only one unique minimum window in s.

Example:
Input: s = "ADOBECODEBANC", t = "ABC"
Output: "BANC"

Solution:
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # We can use sliding window to solve this problem
        # We initailize left and right pointer point to the first char in s
        # Then we move right until s[left:right] contains all the letters we need
        # Move left until s[left:right] not satisfied the requirement
        # Iterate until right pointer points to the end of s
        res = ''
        if not s or not t:
            return res
        
        n = len(s)
        max_len = n
        left, right = 0, 0
        count = 0
        needs = collections.Counter(t)
        while right < n:
            if s[right] in needs:
                needs[s[right]] -= 1
                if needs[s[right]] >= 0:
                    count += 1
        
            right += 1
            while count == len(t):
                if right - left <= max_len:
                    res = s[left:right]
                    max_len = len(res)
                    
                if s[left] in needs:
                    needs[s[left]] += 1
                    if needs[s[left]] > 0:
                        count -= 1
                        
                left += 1
                
        return res
