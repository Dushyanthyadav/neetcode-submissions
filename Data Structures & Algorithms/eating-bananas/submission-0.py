class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:

        l, r = 1, max(piles)
        
        while l <= r:
            k = l + (r - l) // 2
            hours_needed = sum((p + k - 1) // k for p in piles)         
            if hours_needed <= h:
                r = k - 1
            else:
                l = k + 1
        return l