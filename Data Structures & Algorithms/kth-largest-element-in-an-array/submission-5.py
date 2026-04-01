import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        '''
        keep a min heap of size k to pop min value off of that
        while len(heap) > k:
            heapq.heappop(heap)
        return heap[-1]
        '''
        for num in nums:
            heapq.heappush(heap, num)
            while len(heap) > k:
                heapq.heappop(heap)
        return heap[0]

