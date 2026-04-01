class Solution:
    def validPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1
        deleted = False

        while l < r:
            if s[l] != s[r]:
                skipLeft = s[l + 1 : r + 1] # skip left char and go to r (represented as r+1)
                skipRight = s[l : r] #if we skip right, just change r+1 to r and l stays default

                # check if skipLeft array equal to reversal of skipLeft array
                # OR skipRight array equal to skipRight array
                # if both false, return false because impossible
                return skipLeft == skipLeft[::-1] or skipRight == skipRight[::-1]
            l, r = l + 1, r - 1
        return True
            