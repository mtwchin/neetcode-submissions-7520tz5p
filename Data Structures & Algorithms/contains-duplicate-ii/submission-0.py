class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        '''
        the idea is to check for close duplicates under the size of k index
        '''
        # create hashmap of values to indices, keep the most recent index
        h = {}
        for i, val in enumerate(nums):
            if val in h:
                if abs(i - h[val]) <= k:
                    return True
            h[val] = i
        return False
