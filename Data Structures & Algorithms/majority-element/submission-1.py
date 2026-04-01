class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2
        nums.sort()

        curLen = 0
        for i in range(len(nums)):
            if i == 1:
                curLen = 1
            if nums[i] == nums[i - 1]:
                curLen += 1
            if curLen > majority:
                return nums[i]
        