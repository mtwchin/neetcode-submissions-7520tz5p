# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        q = deque()
        res = []
        if not root:
            return res
        else:
            q.append(root)
        
        while q:
            curlevel = []
            qlen = len(q)
            for i in range(qlen):
                node = q.popleft()
                if node:
                    curlevel.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if curlevel:
                res.append(curlevel)
        return res

            