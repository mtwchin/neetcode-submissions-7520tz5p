class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        sort strs to compare first and last string
        '''

        strs = sorted(strs)
        res = ""
        for i in range(len(strs[0])):
            if strs[-1][i] == strs[0][i]:
                res+=(strs[0][i])
            else:
                break
        return res
