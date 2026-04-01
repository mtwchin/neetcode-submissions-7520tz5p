class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # hashmap key=target-value, value=index
        m = {}
        for i, val in enumerate(nums):
            # check if in the hashmap
            if target-val in m:
                return [m[target-val], i]
            m[val] = i