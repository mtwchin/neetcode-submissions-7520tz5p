# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        tracker = 0
        res = None
        def dfs(node):
            nonlocal tracker
            nonlocal res
            if not node:
                return
            dfs(node.left)
            tracker+=1
            if tracker == k:
                res = node.val
                return
            dfs(node.right)
        dfs(root)
        return res
        
        