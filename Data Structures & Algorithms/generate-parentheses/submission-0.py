class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open par. if open < n:
        # only add closed par. if closeCount < openCount
        # BASE CASE: valid IIF open == closed == n:

        stack = []
        res = []

        def backtrack(openC, closedC):
            if openC == closedC == n:
                res.append("".join(stack))
                return
            # add open par.
            if openC < n:
                stack.append("(")
                backtrack(openC + 1, closedC)
                stack.pop()
            if closedC < openC:
                stack.append(")")
                backtrack(openC, closedC + 1)
                stack.pop()
        
        backtrack(0, 0)
        return res

