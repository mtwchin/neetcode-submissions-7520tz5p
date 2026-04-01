# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # B.C 0: 0 nodes, return empty list
        # B.C 1: 1 node, return 1 node as sublist
        # use a queue for bfs, keep track of step so that you can process correct # of nodes
        # example: for step 0, process 1 node and add to sublist
        #       for step 1, process 2 nodes and add to sublist
        #       for step 2, process 4 nodes
        #       for step 3. process 8 nodes

        q = deque()
        res = []
        q.append(root)
        while q:
            width = len(q)
            level = []
            for i in range(width):
                node = q.popleft()
                if node:
                    level.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if level:
                res.append(level)
        return res


