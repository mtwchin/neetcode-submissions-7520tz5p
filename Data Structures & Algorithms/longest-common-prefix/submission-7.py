class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        '''
        sort the list, compare the first from the last string
        loop through and increment count as long as they have a similar prefix
        '''

        strs.sort()
        i = 0
        res = ""

        while i < len(strs[0]) and strs[0][i] == strs[-1][i]:
            res+=(strs[0][i])
            i+=1
        return res