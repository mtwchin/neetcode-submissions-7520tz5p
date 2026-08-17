# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        '''
        1) find the node, binary search
        while root:
            if root.val > key.val:
                root = root.left
            else if root.val < key.val:
                root.right
            else:
                break
        2) delete node:

        '''

        if not root:
            return root
        
        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:
            # found correct node to delete
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            
            # find min from right subtree
            cur = root.right
            while cur.left:
                cur = cur.left
            # cur should be pointing at the minimum node in the right subtree
            root.val = cur.val
            root.right = self.deleteNode(root.right, root.val)
        return root
            
