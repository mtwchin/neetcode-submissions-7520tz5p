# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def dfs(node, curSum):
            # base case
            if not node:
                return False

            curSum += node.val # update sum

            # if leaf, check if the path sum is right
            if not node.left and not node.right:
                return curSum == targetSum
            
            # if a path exists, go there
            return dfs(node.left, curSum) or dfs(node.right, curSum)
        
        
        return dfs(root, 0)