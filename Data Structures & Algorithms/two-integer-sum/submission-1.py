class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        mydict = {}

        for i in range(len(nums)):
            b = target - nums[i]
            if nums[i] in mydict:
                return sorted([i, mydict.get(nums[i])])
            mydict[b] = i
        return [0, 0]

                
        