class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
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
        res = []
        def backtracking(index, path):
            if len(path) == len(digits):
                res.append(path[:])
                return
            for c in digToChar[digits[index]]:
                backtracking(index + 1, path + c)
        
        if digits:
            backtracking(0, "")
        return res