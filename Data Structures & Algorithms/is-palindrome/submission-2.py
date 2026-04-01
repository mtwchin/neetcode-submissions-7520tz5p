class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l+=1
            elif not s[r].isalnum():
                r-=1
            elif s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True




    def isAlphaNum(self, c):
        return (ord("A") <= ord(c) <= ord("Z") or 
                ord("a") <= ord(c) <= ord("z") or
                ord("0") <= ord(c) <= ord("9"))