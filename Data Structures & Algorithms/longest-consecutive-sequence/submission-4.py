class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nnums = sorted(nums)
        maxi, temp = 1, 1
        for i in range(1, len(nnums)):
            if nnums[i] == nnums[i-1] + 1:
                temp+=1
            elif nnums[i] != nnums[i-1]:
                temp = 1
            maxi = max(maxi, temp)
        return maxi
        