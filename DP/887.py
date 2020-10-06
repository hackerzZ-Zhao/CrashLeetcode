Problems:
You are given K eggs, and you have access to a building with N floors from 1 to N. 

Each egg is identical in function, and if an egg breaks, you cannot drop it again.

You know that there exists a floor F with 0 <= F <= N such that any egg dropped at a floor higher than F will break, and any egg dropped at or below floor F will not break.

Each move, you may take an egg (if you have an unbroken one) and drop it from any floor X (with 1 <= X <= N). 

Your goal is to know with certainty what the value of F is.

What is the minimum number of moves that you need to know with certainty what F is, regardless of the initial value of F?

How to hack:
what "under the worst situation" means?
This means the answer is the last try in your algorithm. For example, if you try each floor from 1 to N, the worst case is the answer is N.

The first thought is binary search. However it only works if we have unlimited eggs. In this problem, we have limited eggs. So if we use binary search the eggs may not eought for find out the answer.
For example, if k == 1, you can only do brute force from 1 to N.

So change idea. When we drop the egg on i floor, we only have two results: the egg is broken and the egg is safe.
If the egg is broken, means our k = k - 1 and our answer is located in [1:i] floor
If the egg is safe, means k = k and our answer is located in [i + 1:N] floor
So actually these are the status change in the dp,and we have to keep try each floor in current range of floors.

Base case is easy to find. When K == 1, we can only do brute force from 1 to N, so the answer is N (we need the the answer under worst situation)
When N == 0, the answer is 0

We need to use binary search speed up

Solution:

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        def dp(k, n):
            if k == 1:
                return n
            if n == 0:
                return 0
            if (k, n) in memo:
                return memo[(k, n)]
            
            res = sys.maxsize
            lo, hi = 1, n
            while lo <= hi:
                mid = (lo + hi) // 2
                broken = dp(k - 1, mid - 1) 
                safe = dp(k, n - mid) 
                if broken > safe:
                    hi = mid - 1
                    res = min(res, broken + 1)
                else:
                    lo = mid + 1
                    res = min(res, safe + 1)
                    
            memo[(k, n)] = res
            return res
        
        memo = {}
        return dp(K, N)
