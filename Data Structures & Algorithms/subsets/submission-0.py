class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def r(index, arr):
            if index >= len(nums):
                result.append(arr)
                return
            a = [i for i in arr]
            r(index+1, a)
            b = [i for i in arr]
            b.append(nums[index])
            r(index+1, b)
        r(0, [])
        return result
        