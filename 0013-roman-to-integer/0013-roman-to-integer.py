class Solution:
    def romanToInt(self, s: str) -> int:
        r = {
            'I': 1, 'V': 5, 'X': 10,
          'L': 50, 'C': 100, 'D': 500,
         'M': 1000
         }
        result = 0
        for i in range(len(s)):
            curr = r[s[i]]
            if i+1 < len(s):
                next = r[s[i+1]]
                if curr < next:
                    result -= curr
                else:
                    result += curr
            else:
                result += curr
        return result 
