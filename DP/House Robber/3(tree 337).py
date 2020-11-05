Question:
The thief has found himself a new place for his thievery again. There is only one entrance to this area, called the "root." Besides the root, each house has one and only one parent house. After a tour, the smart thief realized that "all houses in this place forms a binary tree". It will automatically contact the police if two directly-linked houses were broken into on the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.

Example:
Input: [3,2,3,null,3,null,1]

     3
    / \
   2   3
    \   \ 
     3   1

Output: 7 
Explanation: Maximum amount of money the thief can rob = 3 + 3 + 1 = 7.

Solution:
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rob(self, root: TreeNode) -> int:
        # The same idea using dfs
        def dfs(root, memo):
            if not root:
                return 0
            if root in memo:
                return memo[root]
            
            # if rob current house 
            rob_left = dfs(root.left.left, memo) + dfs(root.left.right, memo) if root.left else 0
            rob_right = dfs(root.right.left, memo) + dfs(root.right.right, memo) if root.right else 0

            rob = root.val + rob_left + rob_right
            
            # if not rob current house
            not_rob = dfs(root.left, memo) + dfs(root.right, memo)
            profit = max(rob, not_rob)
            memo[root] = profit
            return profit
        
        memo = {}
        return dfs(root, memo)
    
        # better dfs
        def dfs(root):
            if not root:
                # rob and not rob
                return (0, 0)
            
            left = dfs(root.left)
            right = dfs(root.right)
            # if rob current house, profit == root.val + not_rob_left + not_rob_right
            rob = root.val + left[1] + right[1]
            # if not rob current house, profit == rob_left+ rob_right
            not_rob = max(left) + max(right)
            return (rob, not_rob)
            
        return max(dfs(root))
