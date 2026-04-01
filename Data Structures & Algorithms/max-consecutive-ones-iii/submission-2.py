class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        '''
        two pointer solution with zerosFlipped counter
        '''

        l, zerosFlipped, res = 0, 0, 0
        curLen = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                zerosFlipped += 1
            curLen += 1
            while zerosFlipped > k:
                if nums[l] == 0:
                    zerosFlipped -= 1
                curLen -= 1
                l += 1
            res = max(res, curLen)
        return res
