# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # swap values of immediate bottom subtree
        # base case 0 node: no node, return empty list
        # base case 1 node: no left and no right node so return just the node
        # pre-order: ELR
        if not root:
            return None
        root.left, root.right = root.right, root.left

        self.invertTree(root.right)
        self.invertTree(root.left)
        
        return root
