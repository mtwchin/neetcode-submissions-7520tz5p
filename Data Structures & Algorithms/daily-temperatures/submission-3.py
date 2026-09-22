class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] 
        # to hold pairs of temp -> index, stack by temp but store idx

        for i, t in enumerate(temperatures):
            while stack and t > stack[-1][0]:
                topTemp, topInd = stack.pop()
                res[topInd] = i - topInd
            stack.append((t, i))
        return res