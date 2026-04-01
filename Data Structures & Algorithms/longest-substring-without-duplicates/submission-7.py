class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        res, curLen, l = 0, 0, 0

        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
                curLen -= 1
            charSet.add(s[r])
            curLen += 1
            res = max(res, curLen)
        return res
            
