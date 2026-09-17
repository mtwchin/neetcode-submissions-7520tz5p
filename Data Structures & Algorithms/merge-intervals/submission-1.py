class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        '''
        merge the overlapping intervals
        if they have no common point like [1,2] and [3,4] they are fine
        [[1,3],[1,5],[6,7]]
        
        -> [1,5], [6,7]
        so two intervals are overlapping if the second one starts 
            before the previous one ends
        so walk through with a l and r pointer, iterating both +1
        '''
        intervals = sorted(intervals)
        l, r = 0, 1
        res = [intervals[0]]
        for start, end in intervals[1:]:
            lastStart, lastEnd = res[-1]
            if start <= lastEnd:
                res[-1] = [lastStart, max(lastEnd, end)]
            else:
                res.append([start, end])
        return res

