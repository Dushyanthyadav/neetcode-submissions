class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index = []
        output = [0] * len(temperatures)

        for i in range(len(temperatures)):
            if not stack:
                stack.append(temperatures[i])
                index.append(i)
            else:
                if stack[-1] >= temperatures[i]:
                    stack.append(temperatures[i])
                    index.append(i)
                else:
                    while stack and stack[-1] < temperatures[i]:
                        nex = i - index[-1]
                        output[index.pop()] = nex
                        stack.pop()
                    stack.append(temperatures[i])
                    index.append(i)
             
        return output
