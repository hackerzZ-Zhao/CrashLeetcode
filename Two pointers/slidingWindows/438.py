Question:
Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

The order of output does not matter.

Example:
Input:
s: "cbaebabacd" p: "abc"

Output:
[0, 6]

Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".

Solution:
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # We can using sliding window to solve this problem
        # Just like problem 76, we move the right pointer until s[left:right] contains all the characters we need
        # Then move left pointer and when right - left == len(p), we put left into res which is we need
        # Move left pointer and check whether when we remove this character, s[left:right] still conatins all the letters we need
        
        if not s:
            return []
        
        n = len(s)
        if n < len(p):
            return []
        
        res = []
        left, right = 0, 0
        match = 0
        needs = collections.Counter(p)
        window = collections.defaultdict(int)
        
        while right < n:
            if s[right] in needs:
                window[s[right]] += 1
                if window[s[right]] == needs[s[right]]:
                    match += 1
                
            right += 1
            while match == len(needs):
                if right - left == len(p):
                    res.append(left)
                    
                if s[left] in needs:
                    window[s[left]] -= 1
                    if window[s[left]] < needs[s[left]]:
                        match -= 1
                        
                left += 1
                
        return res
                
