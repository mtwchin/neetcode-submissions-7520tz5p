class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        return k most frequent elements so
        if nums=[1,2,2,3,3,3], k=2
        output = [2,3]

        use min-heap of size k
        '''

        # initialize frequency map
        freq = defaultdict(int)
        for num in nums:
            freq[num] += 1

        # push values onto heap and remove top item if heap too large (min-heap)
        heap = []
        for num in freq.keys():
            heapq.heappush(heap, (freq[num], num))
            if len(heap) > k:
                heapq.heappop(heap)

        # for each item still on the heap, add the number to res ([1]) for 
        #   the second item in the tuple 
        res = []
        for i in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
