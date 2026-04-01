class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:


        l, res, zerosFlipped = 0, 0, 0

        for r in range(len(nums)):
            if nums[r] == 0:
                zerosFlipped += 1
            if zerosFlipped > k:
                if nums[l] == 0:
                    zerosFlipped -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

            
