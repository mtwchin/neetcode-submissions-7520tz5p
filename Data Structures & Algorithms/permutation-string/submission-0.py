class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        dic = {}

        for char in s1:
            # if key char exists in dic, return its value
            # otherwise, return 0
            dic[char] = 1 + dic.get(char,0)
        
        need = len(dic)
        for i in range(len(s2)):
            count2 = {}
            cur = 0
            for j in range(i, len(s2)):
                count2[s2[j]] = 1 + count2.get(s2[j],0)
                if dic.get(s2[j],0) < count2[s2[j]]:
                    break
                if dic.get(s2[j],0) == count2[s2[j]]:
                    cur += 1
                if cur == need:
                    return True
        return False
        
