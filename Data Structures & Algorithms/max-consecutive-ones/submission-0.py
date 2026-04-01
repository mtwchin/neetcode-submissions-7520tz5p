class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxOnes, curLen = 0, 0
        for num in nums:
            if num == 1:
                curLen += 1
            else:
                curLen = 0
            maxOnes = max(curLen, maxOnes)
        return maxOnes