class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles) #start at 1 because bananas/hour = 0 makes no sense
        res = r # at least r must work, max number of banans to eat/hour

        while l <= r:
            k = (l + r) // 2
            hours_eating = 0 # total hours to eat all bananas
            for p in piles:
                hours_eating += math.ceil(p/k)
            if hours_eating <= h:
                res = min(res, k)
                r = k - 1
            else: # if hours_eating > h, then increase speed of eating
                l = k + 1
        return res
