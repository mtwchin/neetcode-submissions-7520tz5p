class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        l, res, curLen = 0, 0, 0
        count = defaultdict(int)
        for r in range(len(fruits)):
            count[fruits[r]] += 1
            curLen += 1

            while len(count) > 2:
                f = fruits[l]
                l += 1
                curLen -= 1
                count[f] -= 1

                if not count[f]:
                    count.pop(f)
            res = max(res, curLen)
        return res