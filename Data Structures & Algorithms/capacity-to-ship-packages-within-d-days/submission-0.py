class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        '''
        binary search problem?
        upper range on ship cap. is sum(weights)
        lower bound on ship cap. is max(weights)  
        '''
        def canShip(cap):
            curCap = cap
            ships = 1
            for w in weights:
                if w - curCap > 0:
                    ships += 1
                    curCap = cap
                curCap -= w
            return ships <= days

        left, right = max(weights), sum(weights)
        res = right
        while left <= right:
            mid = (left + right) // 2 
            if canShip(mid):
                res = min(res, mid)
                right = mid - 1
            else:
                left = mid + 1
        return res


            
