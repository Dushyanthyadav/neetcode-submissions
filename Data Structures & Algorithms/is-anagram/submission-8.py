class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        a1 = {}
        a2 = {}

        for i in range(len(s)):
            if s[i] in a1:
                a1[s[i]] += 1
            else:
                a1[s[i]] = 1
            
            if t[i] in a2:
                a2[t[i]] += 1
            else:
                a2[t[i]] = 1
        
        return a1 == a2
        