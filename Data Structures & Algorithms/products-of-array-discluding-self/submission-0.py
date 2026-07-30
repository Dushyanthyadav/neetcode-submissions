class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = []
        for i in range(len(nums)):
            output = 1
            for j in range(len(nums)):
                if i == j:
                    continue
                output *= nums[j]
            result.append(output)
        return result
        