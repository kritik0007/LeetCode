class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = [c.lower() for c in s if c.isalnum()]
        clean = ''.join(clean)
        rev = clean[::-1]
        if(clean == rev):
            return True
        else:
            return False 