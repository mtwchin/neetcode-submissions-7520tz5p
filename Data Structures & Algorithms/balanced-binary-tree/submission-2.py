# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # get max left and max right
        # if |max left - max right| > 1 return false
        # otherwise true
        def dfs(node):
            if not node:
                return 0
            left_h = dfs(node.left)
            right_h = dfs(node.right)
            return 1 + max(left_h, right_h)
        
        if not root:
            return True
        if abs(dfs(root.left) - dfs(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right):
            return True
        return False
