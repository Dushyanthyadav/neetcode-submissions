class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()
        old = ""
        for letter in lower:
            if letter.isalnum():
                old+=letter

        new = old[::-1]

        if new == old:
            return True
        return False

        