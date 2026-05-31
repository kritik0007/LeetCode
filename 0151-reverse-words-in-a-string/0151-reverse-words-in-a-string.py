class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split()
        x = x[::-1]
        t = ' '.join(x)
        return t