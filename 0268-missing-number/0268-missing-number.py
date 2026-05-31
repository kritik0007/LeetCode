class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n= len(nums)
        sum = 0
        s = 0
        
        sum = (n*(n+1))//2
        for i in nums:
            s = s+i
        t = sum - s
        return t
