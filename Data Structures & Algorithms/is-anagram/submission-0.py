class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        a1 = "".join(sorted(s))
        a2 = "".join(sorted(t))
        if a1 == a2:
            return True
        return False
        