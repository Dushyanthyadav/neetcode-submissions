class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for num in tokens:
            if not num.lstrip("-").isdigit():
                second = stack.pop()
                first = stack.pop()
                if num == "+":
                    stack.append(first + second)
                elif num == "-":
                    stack.append(first - second)
                elif num == "*":
                    stack.append(first * second)
                else:
                    stack.append(int(first/second))
            else:
                stack.append(int(num))

        return stack[-1]
                
                