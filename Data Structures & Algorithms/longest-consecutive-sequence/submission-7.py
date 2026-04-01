class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res, idx, curLen = 0, 0, 0
        nums.sort()

        while idx < len(nums):
            if idx == 0:
                curLen = 1
            elif nums[idx] == nums[idx - 1] + 1:
                curLen += 1
            elif nums[idx] != nums[idx - 1]:
                curLen = 1
            res = max(res, curLen)
            idx+=1
        return res
        