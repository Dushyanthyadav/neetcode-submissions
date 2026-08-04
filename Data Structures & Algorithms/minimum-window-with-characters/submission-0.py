from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        n = len(s)
        original = Counter(t)
        need = len(original)
        have = 0
        check = {}
        lenght = n+1
        small = [-1, -1]
        l = 0
        r = 0
        
        while r < n:
            check[s[r]] = check.get(s[r], 0) + 1

            if s[r] in original and original[s[r]] == check[s[r]]:
                have += 1
            
            while have == need:
                temp = r-l+1
                if temp <= lenght:
                    lenght = temp
                    small = [l, r]

                check[s[l]] -= 1

                if s[l] in original and check[s[l]] < original[s[l]]:
                    have -= 1
                l += 1
            
            r += 1            
        
        if lenght == n+1:
            return ""

        return s[small[0]:small[1]+1]
            
            
