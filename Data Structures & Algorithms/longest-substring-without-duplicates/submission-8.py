class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return n
        longest = 0
        myset = set()
        l = 0
        r = 0
        while r < n:
            if s[r] in myset:
                myset.remove(s[l])
                l += 1
            else:
                myset.add(s[r])
                r += 1
            longest = max(r - l , longest)

        return longest
        

        