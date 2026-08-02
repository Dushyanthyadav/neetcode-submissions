class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        res = 0
        if n == 0:
            return 0
        
        for i in range(len(height)):
            leftMax = rightMax = height[i]

            for j in range(i):
                leftMax = max(leftMax, height[j])
            for j in range(i+1, n):
                rightMax = max(rightMax, height[j])

            res += min(leftMax, rightMax) - height[i]

        return res