from bisect import bisect_left
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        '''
        maintain array dp where dp[i] is the smallest ending elt of all subseq. of length i + 1
        so for each new elt, if its larger than the last elt in dp, it extends the longest subsequence
        otherwise, we just binary search to find the pos. where it can replace an element
        and keep the aray optimal for future extensions

        1. initialize dp with the first elt in the arr
        2. for each elt (nums[i]),
            - if nums[i] > dp[-1], append it to dp
            - otherwise, find the leftmost pos in dp where dp[pos] >= nums[i] w/ binarysearch,
            - and replace dp[pos] with nums[i]
        '''
        dp = []
        dp.append(nums[0])

        lis = 1
        for i in range(1, len(nums)):
            if dp[-1] < nums[i]:
                dp.append(nums[i])
                lis+=1
                continue
            idx = bisect_left(dp, nums[i])
            dp[idx] = nums[i]
        return lis