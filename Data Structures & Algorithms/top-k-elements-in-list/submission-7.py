class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        iterate through and use hashmap{value:count}
        keep minheap of size k
        and if the heap ever exceeds k, pop from top until good size 
        '''

        h = defaultdict(int)
        for num in nums:
            h[num] += 1
        heap = []

        for val, freq in h.items():
            heapq.heappush(heap, (freq, val))
            while len(heap) > k:
                heapq.heappop(heap)
        res = []
        for freq, val in heap:
            res.append(val)
        return res
        