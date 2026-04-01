class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            if len(path) == len(nums):
                res.append(path[:])
                return 
            
            for num in nums:
                if num in path:
                    continue
                
                path.append(num)
                backtrack(index + 1, path)
                path.pop()
        backtrack(0, [])
        return res

        