class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        ss = {}
        tt = {}
        for char in s:
            
                ss[char] = ss.get(char,0)+1
        for char1 in t:
          
               tt[char1] = tt.get(char1,0)+1
        if(ss == tt):
            return True
        else:
            return False 