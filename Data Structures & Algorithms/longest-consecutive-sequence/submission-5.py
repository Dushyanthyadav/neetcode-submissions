class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        a = {}
        
        for i in nums:
            if i not in a:
                a[i] = []
            if i-1 in a:
                a[i-1].append(i)
            if i+1 in a:
                a[i].append(i+1)

        largest = 1
        target_largest = 1

        start = []
        for i in nums:
            if i-1 not in a and i+1 in a:
                start.append(i)
        

        for i in start:
            j = i
            while len(a[j]) != 0:
                target_largest += 1
                j = a[j][-1]
            if largest < target_largest:
                largest = target_largest
            target_largest = 1
        
        return largest

