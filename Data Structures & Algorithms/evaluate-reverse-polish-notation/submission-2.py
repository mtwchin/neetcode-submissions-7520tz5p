class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []
        for c in tokens:
            if c == "+":
                operands.append(operands.pop() + operands.pop())
            elif c == "-":
                a, b = operands.pop(), operands.pop()
                operands.append(b-a)
            elif c == "*":
                operands.append(operands.pop() * operands.pop())
            elif c == "/": 
                a, b = operands.pop(), operands.pop()
                operands.append(int(b / a))
            else:
                operands.append(int(c))
        return operands[0]
            
                