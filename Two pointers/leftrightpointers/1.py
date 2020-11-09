Question:
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Output: Because nums[0] + nums[1] == 9, we return [0, 1].

Solution:
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        if n < 2:
            return []
        
        nums = [(nums[i], i) for i in range(n)]
        nums.sort()
        left, right = 0, n - 1
        while left < right:
            total = nums[left][0] + nums[right][0]
            if total == target:
                return [nums[left][1], nums[right][1]]
            elif total < target:
                left += 1
            else:
                right -= 1
                
        return []
