class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        res = [""]
        digit_char = {
            "2":"abc",
            "3":"def",
            "4":"ghi",
            "5":"jkl",
            "6":"mno",
            "7":"pqrs",
            "8":"tuv",
            "9":"wxyz"
        }

        for dig in digits:
            temp = []
            for curstr in res:
                for c in digit_char[dig]:
                    temp.append(curstr + c)
            res = temp
        return res
