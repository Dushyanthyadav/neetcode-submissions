class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        myset = set(nums)
        start = []
        for i in myset:
            if i-1 not in myset:
                start.append(i)
        largest = 1
        temp_largest = 1
        for i in start:
            a = i
            while a+1 in myset:
                temp_largest += 1
                a = a+1
            if largest < temp_largest:
                largest = temp_largest
            temp_largest = 1

        return largest
        
            

