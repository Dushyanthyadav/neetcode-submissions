from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        original = Counter(s1)
        check = {}
        i = 0
        j = 0
        size = len(s1)
        while j < len(s2):
            check[s2[j]] = check.get(s2[j], 0) + 1
            if j - i + 1 > size:
                check[s2[i]] -= 1
                if check[s2[i]] == 0:
                    del check[s2[i]]
                i += 1
            if original == check:
                return True
            j += 1
            
        return False
        