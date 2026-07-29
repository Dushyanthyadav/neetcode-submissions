class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mydict = {}
        for i in nums:
            if i in mydict:
                return True
            else:
                mydict[i] = 1
        return False
        