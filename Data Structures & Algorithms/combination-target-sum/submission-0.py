class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        base case: When sum of current path == target
        constraints: sum(path) < target, 
        choices: any number
        backtracking step: return and pop back
        return as list of lists
        possibly sort to reduce extra work?
        '''        
        # maybe use set to reject duplicates?
        res = []
        nums.sort()

        def backtrack(i, path, total):
            if total == target:
                res.append(path[:])
                return
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    break
                path.append(nums[j])
                backtrack(j, path, total + nums[j])
                path.pop()
        
        backtrack(0, [], 0)
        return res
        