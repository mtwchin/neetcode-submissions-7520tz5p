# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        if not preorder or not inorder:
            return None
        
        node = TreeNode(preorder[0], None, None)
        pivotInd = inorder.index(preorder[0])

        node.left = self.buildTree(preorder[1:pivotInd+1], inorder[:pivotInd])
        node.right = self.buildTree(preorder[pivotInd+1:], inorder[pivotInd+1:])


        return node

