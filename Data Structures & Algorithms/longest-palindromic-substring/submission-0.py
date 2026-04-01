class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""
        resLen = 0

        for center in range(len(s)):
            # odd length. i is center pos
            l, r = center, center
            # while l and r pts in bound, AND
            #   while valid palindrome,
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l -= 1
                r += 1
            
            # even length palindromes
            l, r = center, center + 1
            while l>= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > resLen:
                    res = s[l:r + 1]
                    resLen = r - l + 1
                l-=1
                r+=1
        return res