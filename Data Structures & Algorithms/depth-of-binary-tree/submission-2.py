# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        
        # if root is null, return 0 b/c it contributes nothing to depth
        if not root:
            return 0
        
        # recursive solution, check left, then right subtree
        left = self.maxDepth(root.left)
        right = self.maxDepth(root.right)
        
        # +1 because leaf nodes contribute 1 to maxdepth
        return max(left,right) + 1