# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        '''
        DFS (use visited set)
        '''
        visited = set()

        def dfs(pathSum, node):
            if not node:
                return False
            pathSum += node.val
            if not node.left and not node.right:
                return pathSum == targetSum
            
            return dfs(pathSum, node.left) or dfs(pathSum, node.right)
        
        return dfs(0, root)
            