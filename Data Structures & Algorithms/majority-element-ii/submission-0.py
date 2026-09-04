import heapq
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        hashmap for value to count
        keep a max heap of size n/3
        '''
        res = []
        freq = defaultdict(int)
        for num in nums:
            freq[num]+=1
        
        for key, val in freq.items():
            if val > len(nums)//3:
                res.append(key)
        return res