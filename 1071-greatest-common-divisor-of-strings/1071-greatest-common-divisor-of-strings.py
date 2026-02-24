import math

class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        # Check if a valid divisor exists
        if str1 + str2 != str2 + str1:
            return ""
        
        # Compute GCD of lengths
        gcd_length = math.gcd(len(str1), len(str2))
        
        # Return prefix of that length
        return str1[:gcd_length]