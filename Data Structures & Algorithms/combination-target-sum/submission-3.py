class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        #nums.sort()

        def r(s, i, arr):
            if s == target:
                res.append(arr.copy())
                return

            for j in range(i, len(nums)):
                if s + nums[j] > target:
                    continue
                arr.append(nums[j])
                r(s+nums[j], j, arr)
                arr.pop()
        r(0, 0, [])

        return res
