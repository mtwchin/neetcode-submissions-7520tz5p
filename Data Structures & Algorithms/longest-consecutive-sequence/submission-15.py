class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        '''
        must run in O(n) so no sorting
        nums = [2,20,4,10,3,4,5]
        use a set, if curNum - 1 is in the set 
        '''
        numSet = set(nums)
        longest = 0

        for num in nums:
            if not (num - 1) in numSet:
                curlen = 0
                i = 0
                while num + i in numSet:
                    curlen += 1
                    i += 1
                longest = max(curlen, longest)
        return longest