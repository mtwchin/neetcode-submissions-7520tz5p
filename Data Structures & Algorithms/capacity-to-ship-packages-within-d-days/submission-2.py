class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        res = right


        def canShip(cap):
            curCap = cap
            ships = 1
            for w in weights:
                if curCap - w < 0:
                    ships += 1
                    curCap = cap
                curCap -= w
            return ships <= days
        
        while left <= right:
            mid = (left + right) // 2
            if canShip(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res