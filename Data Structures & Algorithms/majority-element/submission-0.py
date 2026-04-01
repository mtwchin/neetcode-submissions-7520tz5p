class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # sort nums (O(nlogn))
        nums.sort()
        return nums[len(nums) // 2]