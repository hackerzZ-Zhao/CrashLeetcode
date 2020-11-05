Question:
Koko loves to eat bananas.  There are N piles of bananas, the i-th pile has piles[i] bananas.  The guards have gone and will come back in H hours.

Koko can decide her bananas-per-hour eating speed of K.  Each hour, she chooses some pile of bananas, and eats K bananas from that pile.  If the pile has less than K bananas, she eats all of them instead, and won't eat any more bananas during this hour.

Koko likes to eat slowly, but still wants to finish eating all the bananas before the guards come back.

Return the minimum integer K such that she can eat all the bananas within H hours.

Example:
Input: piles = [3,6,7,11], H = 8
Output: 4

Solution:
class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        # The speed should be in the range (1, max(piles))
        # So we try different from 1 to max(piles), when we find one speed satisfied the requirement
        # this is the speed we want
        # we can use binary search to improve time complexity
        def cal(total, speed):
            rest = 1 if total % speed > 0 else 0
            return total // speed + rest
        
        def canFinish(piles, speed, H):
            time = 0
            for pile in piles:
                time += cal(pile, speed)
                
            return time <= H
        
        left, right = 1, max(piles)
        while left <= right:
            mid = left + (right - left) // 2
            if canFinish(piles, mid, H):
                right = mid - 1
            else:
                left = mid + 1
                
        return left
    
