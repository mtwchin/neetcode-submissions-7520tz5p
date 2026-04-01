class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(index, path):
            if index == len(nums):
                res.append(path[:])
                return
            
            # recursive backtracking,
            # Decision 1: add and continue
            path.append(nums[index])
            backtrack(index + 1, path)
            
            
            path.pop()

            # Decision 2: just continue
            backtrack(index + 1, path)
        backtrack(0, [])
        return res