# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        basically the idea is to get the rightmost node at each level
        go through the tree level by level and take the rightmost node
        probably iterative solution, not recursive because you
            can't really break this problem up into subtrees
        maybe recurse with level indexing?
        '''
        res = []
        def dfs(node, level):
            if not node:
                return None
            if level == len(res):
                res.append(node.val)

            dfs(node.right, level + 1)
            dfs(node.left, level + 1)
        dfs(root, 0)
        return res
        
