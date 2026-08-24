# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        '''
        probably going to be some type of recursive BFS (?)
        might need to keep track of node level to ensure we only use   
            1 node from each level
        return the values of the nodes, so return a list
        '''
        q = deque()
        q.append(root)
        res = []
        while q:
            rightSide = None # there's only 1 rightmost node for each level
            qlen = len(q)
            curlevel = []
            for i in range(qlen): # for each value in the level
                node = q.popleft() 
                if node: # if node at the top of the q exists, set it to rightside
                    rightSide = node
                    q.append(node.left)
                    q.append(node.right)
            if rightSide: # last node value will be rightside
                res.append(rightSide.val)
        return res

