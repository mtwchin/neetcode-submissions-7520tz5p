class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        return k most frequent elements so
        if nums=[1,2,2,3,3,3], k=2
        output = [2,3]

        use min-heap of size k
        '''

        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
