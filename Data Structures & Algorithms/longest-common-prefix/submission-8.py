class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strs = sorted(strs)
        s1, s2 = strs[0], strs[-1]
        res = ""
        i = 0
        while i < len(s1) and i < len(s2):
            if s1[i] == s2[i]:
                res+=(s1[i])
            else:
                break
            i+=1
        return res
