class Solution:
    def isPalindrome(self, s: str) -> bool:
        text = ""

        for c in s:
            if c.isalnum():
                text += c

        text = text.lower()

        match = True

        start = 0
        end = len(text) - 1
        while start < end:
            if text[start] != text[end]:
                match = False
                break
                
            start += 1
            end -= 1

        return match
