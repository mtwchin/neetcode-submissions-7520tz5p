class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        '''
        frequency array = counts1 = [0] * 26        
        iterate through s2, make new array to compare
        '''
        l = 0
        # create frequency array
        s1freq = [0] * 26
        for char in s1:
            s1freq[ord(char) - ord('a')] += 1
        s2freq = [0] * 26
        for r in range(len(s2)):
            curCharAsc = ord(s2[r]) - ord('a')
            s2freq[curCharAsc] += 1
            # while the s1 freq array does not contain the current s2[left] character, increm. l
            while r - l + 1 > len(s1):
                s2freq[ord(s2[l]) - ord('a')] -= 1
                l += 1
            if s2freq == s1freq:
                return True
        return False