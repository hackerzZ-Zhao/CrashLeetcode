Question:
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Solution:
class Solution:
    def trap(self, height: List[int]) -> int:
#         # for each position, it can contains water[i] = min(max(height[0:i]), max(height[i + 1:])) - height[i]
#         # based on this, we can have a brute force solution
#         n = len(height)
#         res = 0
#         for i in range(1, n - 1):
#             left_max, right_max = max(height[:i]), max(height[i + 1:])
#             water = min(left_max, right_max) - height[i] 
#             res += water if water >= 0 else 0
            
#         return res
    
        # the time complexity of brute force would be O(n ** 2) and we can improve it by using memorization
        # we use two array to record left_max and right_max in advance so we can reduce duplicate calculation
#         n = len(height)
#         if n == 0:
#             return 0
#         res = 0
#         left_max, right_max = [0] * n, [0] * n
#         left_max[0] = height[0]
#         right_max[n - 1] = height[n - 1]
#         for i in range(1, n):
#             left_max[i] = max(left_max[i - 1], height[i])
#         for i in range(n - 2, -1, -1):
#             right_max[i] = max(right_max[i + 1], height[i])
            
#         for i in range(1, n - 1):
#             water = min(left_max[i], right_max[i]) - height[i]
#             res += water if water >= 0 else 0
            
#         return res
    
        # After using memorization, we can reduce the time complexity from O(n ** 2) to O(n)
        # But the space complexity is O(n) since we use two array with length n
        # We can keep improving our solution to O(n) time + O(1) space by using two pointer
        n = len(height)
        if n == 0:
            return 0
        
        left, right = 0, n - 1
        res = 0
        left_max, right_max = height[0], height[n - 1]
        while left <= right:
            left_max = max(left_max, height[left])
            right_max = max(right_max, height[right])
            
            if left_max < right_max:
                res += left_max - height[left]
                left += 1
            else:
                res += right_max - height[right]
                right -= 1
                
        return res
