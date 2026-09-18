class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l, r = 0, 0
        minlen, total = float("inf"), 0

        while r < len(nums):
            total += nums[r]
            while total >= target:
                minlen = min(minlen, r - l + 1)
                total -= nums[l]
                l += 1
            r += 1
        if minlen == float("inf"):
            return 0 
        else:
            return minlen

        