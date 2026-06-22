class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        match = {')':'(',']':'[','}':'{'}
        for char in s:
            if char in match:
                if not seen:
                    return False
                if seen[-1] == match[char]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(char)
        return len(seen) == 0


