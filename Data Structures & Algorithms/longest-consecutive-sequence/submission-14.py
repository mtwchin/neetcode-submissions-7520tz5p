class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        sort the list, then two pointer holding a maxlen value
        '''
        nums = sorted(nums)
        maxSeq = 0
        curSeq = 1
        if not nums:
            return 0
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]: # if consecutive numbers are equal
                continue
            elif nums[i] == nums[i -1] + 1: # if cur and prev are consecutive
                    curSeq += 1
            else:
                curSeq = 1
            maxSeq = max(maxSeq, curSeq)
        return max(maxSeq, curSeq)
