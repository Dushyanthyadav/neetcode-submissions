class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)%2 == 1:
            return False

        bracket = {")": "(", "}": "{", "]": "["}

        stack = []

        for l in s:
            if not stack and l in bracket:
                return False
            else:
                if l in bracket:
                    if bracket[l] != stack[-1]:
                        return False
                    stack.pop()
                else:
                    stack.append(l)
        if len(stack) == 0:
            return True
        else: 
            return False
            