class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l = 0
        total = 0
        minlen = float("inf")
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                minlen = min(r - l + 1, minlen)
                total -= nums[l]
                l += 1
        if minlen == float("inf"):
            return 0
        else:
            return minlen

        