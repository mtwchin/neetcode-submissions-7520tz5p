class Solution:
    def maxProfit(self, prices: List[int]) -> int:
       slow, fast, maxi = 0, 1, 0
       while fast < len(prices):
        if prices[slow] < prices[fast]:
            profit = prices[fast] - prices[slow]
            maxi = max(maxi,profit)
        else:
            slow = fast
        fast += 1
       
       return maxi 