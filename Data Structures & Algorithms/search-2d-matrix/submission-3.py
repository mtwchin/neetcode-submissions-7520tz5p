class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # iterate through arrays, check curlist[-1]
        # if curlist[-1] < target, move right
        # if curlist[-1] > target inspect current array
        # if curlist[-1] == target, return 

        for curlist in matrix:
            if curlist[-1] < target:
                continue
            else:
                l, r = 0, len(curlist) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if curlist[mid] > target:
                        r = mid - 1
                    elif curlist[mid] < target:
                        l = mid + 1
                    else:
                        return True
                return False
        return False
                    
