class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0
        for i in range(len(height)):
            while stack and height[i] >= height[stack[-1]]:
                bottom = height[stack.pop()]
                if stack:
                    trap = min(height[stack[-1]], height[i]) - bottom
                    res += trap * (i - stack[-1] - 1)
            stack.append(i)

        return res