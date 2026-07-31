class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        sorted_list = sorted(nums)
        largest=1
        temp_largest = 1
        for i in range(1, len(sorted_list)):
            if sorted_list[i-1] == sorted_list[i]:
                continue
            elif sorted_list[i-1] == sorted_list[i] - 1:
                temp_largest += 1
                if temp_largest > largest:
                    largest = temp_largest
            else:
                temp_largest = 1
        return largest