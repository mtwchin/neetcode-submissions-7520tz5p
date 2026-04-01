class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        n = len(s) # right pointer

        for i in range(n // 2):
            if s[i] != s[n - i - 1]:
                return False
        return True
        