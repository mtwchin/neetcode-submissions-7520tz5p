class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        sta = []
        for val in tokens:
            if val == "+":
                sta.append(sta.pop() + sta.pop())
            elif val == "-":
                a,b = sta.pop(), sta.pop()
                sta.append(b-a)
            elif val == "*":
                sta.append(sta.pop() * sta.pop())
            elif val == "/":
                a,b = sta.pop(), sta.pop()
                sta.append(int(float(b) / a))
            else:
                sta.append(int(val))
        return sta[0]
            