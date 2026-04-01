class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        st, en, maxi = 0, 0, 0
        subset = set()
        while en < len(s):
            if s[en] not in subset:
                subset.add(s[en])
                en+=1
                maxi = max(maxi, en - st)
            else:
                subset.remove(s[st])
                st +=1 
        return maxi

            