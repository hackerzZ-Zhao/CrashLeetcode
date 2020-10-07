An optimization for 887(1)

Previous solution is easy to understand but ineffective. We can try to analyze the problem in a different way.

Under worst situation, in given k eggs and n floors, return the minimum number of test to find out that floor ==>
given k eggs and allow you test at most m times, what is the maximum number of floor can you test at most under worst situation

This time we use a reverse idea. if dp[k][m] == i means givne k eggs and allow you try at most m times, you can find out the answer in i floors height building,
then when dp[K][m] == N, it means given K eggs and allow you try at most m times, you can find out the answer in N floors height building. The num m is what we want.

So what is the state transition equation?

Based on this dp definition, we got two facts:
1. if we throw the egg on floor i and the egg is not broken, we go to test [i + 1: N], otherwise we go to test [1: i - 1]
2. the total floors we can test == the floors above current floor + the floors beneath currrent floor + 1 (current floor)

So we have:
dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
dp[k - 1][m - 1] represents the egg is broken so available egg - 1 and the total times of trying - 1 too
dp[k][m - 1] represents the egg is safe and the total times of trying - 1

Solution:

class Solution:
    def superEggDrop(self, K: int, N: int) -> int:
        # dp[k][m] means the number floors can be identify when using k egges with maximum try m times 
        dp = [[0 for col in range(N + 2)] for row in range(K + 2)]
        m = 0
        while dp[K][m] < N:
            m += 1
            for k in range(1, K + 1):
                dp[k][m] = dp[k - 1][m - 1] + dp[k][m - 1] + 1
                
        return m


