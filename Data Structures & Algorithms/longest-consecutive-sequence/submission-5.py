class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        #conver to set
        num_set = set(nums)
        maxi = 0
        for val in num_set:    
            # if curval-1 doesnt exist, start of new sequence
            if (val - 1) not in num_set:
                # curlen is 1, include current value
                cur_len = 1
                # set, so no need to iterate linearly
                # just increase temp var while consecutive
                # values keep existing, check += 1
                while (val + cur_len) in num_set:
                    cur_len += 1
                # Update max value if needed, after consec. checking
                maxi = max(cur_len, maxi)
        return maxi
        