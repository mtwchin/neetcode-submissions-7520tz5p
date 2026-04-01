class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        # basically asking to implement a sorting algorithm in one pass
        count = [0] * 3
        for num in nums:
            count[num] += 1
        index = 0
        for n in range(3):
            while count[n]:
                count[n] -= 1
                nums[index] = n
                index += 1

        