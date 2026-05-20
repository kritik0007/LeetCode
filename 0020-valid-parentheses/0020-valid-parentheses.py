class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        matches = {')':'(',']':'[','}':'{'}
        for char in s:
            if char in matches:
                if not stack:
                    return False
                if stack[-1]==matches[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)    
        return len(stack) == 0