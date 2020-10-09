Problems:
Alex and Lee play a game with piles of stones.  There are an even number of piles arranged in a row, and each pile has a positive integer number of stones piles[i].

The objective of the game is to end with the most stones.  The total number of stones is odd, so there are no ties.

Alex and Lee take turns, with Alex starting first.  Each turn, a player takes the entire pile of stones from either the beginning or the end of the row.  This continues until there are no more piles left, at which point the person with the most stones wins.

Assuming Alex and Lee play optimally, return True if and only if Alex wins the game.

Examples:
Input: piles = [5,3,4,5]
Output: true
Explanation: 
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.

how to hack:
The problem requires us to simulate a smart person to do the choice. These kind of problem always need use dp to do.
So each time we only two choices:left or right, we should not choose based on current value, as a smart guy, we should consider all the values we would get before we make a decision.
We want Alex win, in other words, when the game is end, the number of stones from Alex is more than Lee. 
So define dp[i][j] represents the maximum different of Alex and Lee when facing piles[i:j + 1] and Alex pick first.
base case is easy, when i == j, we have only one pile, so dp[i][j] == piles[i]

dp[i][j] = max(piles[i] - dp[i + 1][j], piles[j] - dp[i][j - 1]) 

Solution:
class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        f = [[0 for _ in range(n)] for _ in range(n)]
        
        for i in range(n):
            f[i][i] = piles[i]
        
        for i in range(n - 1, -1, -1):
            for j in range(i + 1, n):
                f[i][j] = max(piles[i] - f[i + 1][j], piles[j] - f[i][j - 1])
        
        return f[0][n - 1] > 0
