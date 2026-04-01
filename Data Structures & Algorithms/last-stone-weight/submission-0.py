class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # use max heap to solve, so push values as negative and 
        # perform arithmetic negative wise
        maxheap = [-s for s in stones]
        heapq.heapify(maxheap)

        while len(maxheap) > 1:
            first, second = heapq.heappop(maxheap), heapq.heappop(maxheap)
            if second > first:
                heapq.heappush(maxheap, first - second)
        maxheap.append(0)
        return abs(maxheap[0])
        

