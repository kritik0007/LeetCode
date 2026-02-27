class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        current = 0
        highest = 0
        
        for g in gain:
            current += g
            highest = max(highest, current)
        
        return highest