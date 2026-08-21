# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        starting with the root node, add the left then right as a sublist to res
        then recurse further
        bfs
        use a queue to manage which nodes we process
        if not root, return []

        at each step, process all queue contents, then add L and R to the queue
        '''

        q = deque()
        res = []
        if not root:
            return res
        else:
            q.append(root)
        while q:
            qlen = len(q)
            curlevel = []
            for i in range(qlen):
                node = q.popleft()
                if node:
                    curlevel.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if curlevel:
                res.append(curlevel)
        return res
            