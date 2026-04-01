class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        curSum = 0
        minlen = float('inf')
        for r in range(len(nums)):
            curSum += nums[r]
            while curSum >= target:
                minlen = min(minlen, r - l + 1)
                curSum -= nums[l]
                l += 1
        if minlen != float('inf'):
            return minlen
        else:
            return 0
            