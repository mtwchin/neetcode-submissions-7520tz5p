class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        '''
        2 pointer with set
        '''
        charSet = set()
        maxlen = 0
        l = 0
        for r in range(len(s)):
            # if cur char not in the set, add to it and increase len
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxlen = max(maxlen, r - l + 1)
        return maxlen


