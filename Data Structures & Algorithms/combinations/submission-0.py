class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        # base case: when path len == k
        # choices: all numbers from 1, n
        # constraints: no re-using numbers, at most k length path
        # backtracking step: pop last number, path+=1, continue
        res = []

        def backtrack(start, path):
            if len(path) == k:
                res.append(path[:])
                return
            
            for num in range(start, n + 1):
                path.append(num)
                backtrack(num + 1, path)
                path.pop()
        
        backtrack(1, [])
        return res
