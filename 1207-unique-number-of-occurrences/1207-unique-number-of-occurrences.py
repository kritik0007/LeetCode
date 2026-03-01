class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        count = {}
        
        # Count frequency
        for num in arr:
            count[num] = count.get(num, 0) + 1
        
        # Check uniqueness of frequencies
        frequencies = count.values()
        return len(frequencies) == len(set(frequencies))