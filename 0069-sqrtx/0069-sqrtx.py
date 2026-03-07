class Solution:
    def mySqrt(self, x: int) -> int:
        if(x == 0 or x == 1):
            return x
        l = 1
        h = x
        while(l<=h):
            m = l+(h-l)//2
            if(m*m==x):
                return m
            elif(m*m<x):
                l = m+1
            else:
                h = m - 1
        return h