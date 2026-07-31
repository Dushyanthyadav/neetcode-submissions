class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        old = ""
        for letter in lower:
            if letter.isalnum():
                old+=letter

        n = len(old)

        i = 0
        j = n-1
        while i <= j:
            if old[i] == old[j]:
                i += 1
                j -= 1
                continue
            else:
                return False
        return True
        