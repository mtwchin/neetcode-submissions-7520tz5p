class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r,maxarea = 0, len(heights)-1, 0
        while l < r:
            cur = (r-l) * min(heights[r],heights[l])
            maxarea = max(maxarea, cur)
            if heights[l] < heights[r]:
                l+=1
            else:
                r-=1
        return maxarea