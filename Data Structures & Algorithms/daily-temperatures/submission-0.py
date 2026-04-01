class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        arr = [0]*len(temperatures)
        stack = [] #will contain pair of [temp,index]

        for i, val in enumerate(temperatures):
            while stack and val > stack[-1][0]:
                stackTemp, stackInd = stack.pop()
                arr[stackInd] = (i - stackInd)
            stack.append([val, i])
        return arr



                