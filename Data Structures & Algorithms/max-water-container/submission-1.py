class Solution:
    def maxArea(self, heights: List[int]) -> int:
        largest = 0
        i = 0
        j = len(heights) - 1
        while i < j:
            small = min(heights[i], heights[j])
            cap = small*(j-i)
            if largest < cap:
                largest = cap
            if heights[i] == small:
                i+=1
            else:
                j-=1
        
        return largest