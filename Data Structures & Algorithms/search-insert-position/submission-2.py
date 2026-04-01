class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        binary search, if mid == target, return index
        nums=[-1,0,2,5,6] target = 1
        l = 0, r = 4
        mid = 2
        '''
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                l = mid + 1
            else:
                r = mid - 1
        # what if we never find target?
        return l

        '''
         [2] target=1
        r l
        [2,3] target=3
         r l
        '''