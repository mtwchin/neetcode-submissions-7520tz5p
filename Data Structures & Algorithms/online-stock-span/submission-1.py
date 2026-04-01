class StockSpanner:
    '''
    use a stack to track the most recent prices
    at each next call, pop from stack until invalid then append back on
    '''
    def __init__(self):
        self.stack = []


    def next(self, price: int) -> int:
        res = 1
        while self.stack and self.stack[-1][0] <= price:
            res += self.stack.pop()[1]
        self.stack.append((price, res))
        return res
# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)