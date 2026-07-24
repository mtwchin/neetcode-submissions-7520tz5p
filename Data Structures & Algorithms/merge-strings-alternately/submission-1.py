class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        '''
        maybe 2 pointer
        - while the character at the pointer exists, append to res
        - if one of the pointers has no characters, append the rest of the string from cur to [-1]
            to res
        
        '''

        p = 0
        res = ""
        while p < len(word1) and p < len(word2):
            res+=(word1[p])
            res+=(word2[p])
            p+=1
        # this goes until one of the words is done
        while p < len(word1) or p < len(word2):
            if p < len(word1):
                res+=(word1[p])
            if p < len(word2):
                res+=(word2[p])
            p+=1
        
        return res