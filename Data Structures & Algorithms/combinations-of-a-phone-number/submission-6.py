class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        digToChar = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz",
        }

        def backtrack(index, s):
            if len(s) == len(digits):
                res.append(s[:])
                return
            
            for char in digToChar[digits[index]]:
                backtrack(index + 1, s + char)
        
        if digits:
            backtrack(0, "")
        return res