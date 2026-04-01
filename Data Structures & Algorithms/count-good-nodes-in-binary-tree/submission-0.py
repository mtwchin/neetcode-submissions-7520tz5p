# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        '''
        track outputs:
        dfs(root, 2)
        node.val = 2
        pathmax = 2
        dfs(node.left, 2)

        '''

        def dfs(node, pathMax):
            if not node:
                return 0
            pathMax = max(node.val, pathMax)
            if node.val >= pathMax:
                return 1 + dfs(node.left, pathMax) + dfs(node.right, pathMax)
            else:
                return dfs(node.left, pathMax) + dfs(node.right, pathMax)
        
        return dfs(root, root.val)

