class Solution:
    def search(self, nums: List[int], target: int) -> int:
        '''
        [3,4,1,2], target = 1
        '''

        for i, val in enumerate(nums):
            if val == target:
                return i
        return -1