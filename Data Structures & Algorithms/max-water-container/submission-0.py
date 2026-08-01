class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        for i in range(len(heights)):
            for j in range(i+1, len(heights)):
                small = min(heights[i], heights[j])
                cap = small*(j-i)
                if cap > largest:
                    largest = cap
        
        return largest