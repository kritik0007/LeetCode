class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxx = 1
        minn = 1
        result = float('-inf')
        for num in nums:
            temp = maxx
            maxx = max(num,num*maxx,num*minn)
            minn = min(num,num*temp,num*minn)
            result = max(result,maxx)
        return result 