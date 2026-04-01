class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        '''
        return top k frequent elements in the array
        make heap of size k
        store tuples of (value, count)
        '''
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
        heap = []
        # iterate through all possible values
        for num in count.keys():
            heapq.heappush(heap, (count[num], num)) # push count, num tuple onto the heap
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        for count, num in heap:
            res.append(num)
        return res
        