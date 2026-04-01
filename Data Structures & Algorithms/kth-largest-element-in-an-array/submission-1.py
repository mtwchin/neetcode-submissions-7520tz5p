import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        '''
        [2,3,1,5,4], k=2
        1,2,3,4,5 so return 4
        create heap of size k initialized with 0s, for each element in the array
            if nums[i] > heap[-1]:
                add nums[i] to heap and heapify
        after iterating through the entire
        '''
        heap = nums[:k]
        heapq.heapify(heap)
        for val in nums[k:]:
            # iterate through nums, if val > smallest value in minheap,
            # pop that number off, push the new value maintaining min-heap

            if val > heap[0]:
                heapq.heappop(heap)
                heapq.heappush(heap, val)
        return heap[0]
        

