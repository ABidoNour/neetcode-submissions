class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        ops = set(['+','-','*','/'])
        stack = []
        for tok in tokens:
            if tok in ops:
                num2 = stack.pop()
                num1 = stack.pop()
                if tok == '+':
                    new = num1 + num2
                elif tok == '-':
                    new = num1 - num2
                elif tok == '*':
                    new = num1 * num2
                else:
                    new = int(num1 / num2)
                stack.append(new)
            else:
                stack.append(int(tok))
        return stack.pop()