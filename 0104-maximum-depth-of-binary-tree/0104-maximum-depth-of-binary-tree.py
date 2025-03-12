# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(n, depth):
            if n is None:
                return depth
            
            return max(dfs(n.left, depth+1), dfs(n.right, depth+1))
        return dfs(root, 0)
        