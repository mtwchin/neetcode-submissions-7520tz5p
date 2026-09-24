import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        - keep a heap of size k to hold the closest pts / least E.D
        - maybe heap pts as [E.D, tuple]
        '''
        heap = []
        for xi, yi in points:
            ed = (xi ** 2) + (yi ** 2)
            heap.append([ed, xi, yi])
        
        heapq.heapify(heap)

        res = []

        while k > 0:
            dist, x, y = heapq.heappop(heap)
            res.append([x, y])
            k -= 1
        return res