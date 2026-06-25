class Solution:
    def longestPalindrome(self, s):
        result = ""
        for i in range(len(s)):
            odd = self.expand(s, i, i)       
            if len(odd) > len(result):        
                result = odd
            even = self.expand(s, i, i+1)    
            if len(even) > len(result):       
                result = even
        return result

    def expand(self, s, left, right):
        while left>=0 and right<len(s) and s[left]==s[right]:  
            left -= 1
            right += 1
        return s[left+1:right]



        