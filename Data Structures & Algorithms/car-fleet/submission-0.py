class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted([(pos, spe) for pos, spe in zip(position, speed)], reverse=True)
        stack = []
        for car in cars:
            pos = car[0]
            spe = car[1]
            time = (target - pos) / spe
            if stack:
                if time > stack[-1]:
                    stack.append(time)
            else:
                stack.append(time)
                
        return len(stack)
        