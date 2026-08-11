class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        pivot = 0
        while left < right:
            m = (left + right) // 2
            if nums[m] > nums[right]:
                left = m + 1
            else:
                right = m

        pivot = left

        l, r = 0, len(nums) - 1

        if target >= nums[pivot] and target <= nums[r]:
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] < target:
                l = m + 1
            else:
                r = m - 1
            
             
                 
             
        return -1
        