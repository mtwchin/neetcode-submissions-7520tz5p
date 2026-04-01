class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        '''
        maybe use some type of prefix or suffix sum combo?
        eg: nums = [2, -1, 1, 2], k = 2 and output = 4
                    because [2], [2, -1, 1], and [-1, 1, 2] and [2]
        prefx: [2, 1, 2, 4]
        all combos where nums[i] - prefix[i]

        '''


        res = 0
        curSum = 0

        prefixSums = {0 : 1}
        for n in nums:
            curSum += n
            diff = curSum - k
            res += prefixSums.get(diff, 0)
            prefixSums[curSum] = 1 + prefixSums.get(curSum, 0)
        
        return res
