class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * (len(nums))
        pref = 1

        for i in range(len(nums)):
            res[i] = pref
            pref *= nums[i]
        
        post = 1
        # range(len(nums)-1) = start at last index
        # stop = -1 so stop before hitting -1
        # step = -1 so step -1 each iteration
        # so if len(nums) = 4, does this:
        #           i=3,2,1,0

        # so basically for each number iterating backwards,
        for i in range(len(nums) -1, -1, -1):
            # mult. each res[#] by the postfix (currently 1)
            res[i] *= post
            # increment the postfix
            post *= nums[i]
        return res
