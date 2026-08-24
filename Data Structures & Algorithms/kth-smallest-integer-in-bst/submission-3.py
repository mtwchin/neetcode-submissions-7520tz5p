# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import heapq
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        '''
        min-heap of size k (return minHeap[-1])
        could do bfs or dfs, just need to traverse the entire tree
        '''
        maxHeap = []
        def dfs(node):
            if not node:
                return
            heapq.heappush(maxHeap, -node.val)
            if len(maxHeap) > k:
                heapq.heappop(maxHeap)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return -maxHeap[0]

