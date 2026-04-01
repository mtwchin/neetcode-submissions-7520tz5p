class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # loop through the first value of each string
        # - store cur char of first string,
        # - compare to rest of strings in array
        # - also store amount of iterations
        # return the amount
        if len(strs) == 1:
            return strs[0]
        strs=sorted(strs)

        for i in range(min(len(strs[0]), len(strs[-1]))):
            if strs[0][i] != strs[-1][i]:
                return strs[0][:i]
        return strs[0]
