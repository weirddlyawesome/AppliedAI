class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = ""

        for char in s.lower():
            if char.isalnum():
                cleaned += char


        if cleaned == cleaned[::-1]:
            return True

        return False