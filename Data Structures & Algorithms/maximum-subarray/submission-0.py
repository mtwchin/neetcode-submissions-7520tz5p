class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        '''
        probably two pointer solution.
        - start l @ 0 and r @ end
        - start l @ 0 and r @ 1
        sliding window or decreasing window (?)

        keep running maxsum
        iterate through the array

        '''

        res = nums[0]
        n = len(nums)
        for i in range(n):
            curSum = 0
            for j in range(i, n):
                curSum += nums[j]
                res = max(res, curSum)
        return res