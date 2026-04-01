class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         list_output = list(set(nums));
         if(len(list_output) != len(nums)):
            return True
         else:
            return False