class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        lps = [0] * n
        
        i = 0
        j = 1
        
        while j < n:
            if s[i] == s[j]:
                i += 1
                lps[j] = i
                j += 1
            else:
                if i == 0:
                    lps[j] = 0
                    j += 1
                else:
                    i = lps[i - 1]
        
        if lps[n - 1] == 0:
            return ""
        
        start = n - lps[n - 1]
        return s[start:]