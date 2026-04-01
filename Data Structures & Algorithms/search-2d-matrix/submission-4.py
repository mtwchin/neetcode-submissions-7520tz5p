class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for clist in matrix:
            if clist[-1] < target:
                continue
            else:
                # then run binary search on current list
                # because you know target is within curlist
                l, r = 0, len(clist) - 1
                while l <= r:
                    mid = (l + r) // 2
                    if clist[mid] < target:
                        l = mid + 1
                    elif clist[mid] > target:
                        r = mid - 1
                    else:
                        return True
        return False

                    
