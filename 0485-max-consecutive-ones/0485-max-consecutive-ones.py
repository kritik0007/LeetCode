class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        curr = 0
        max_count = 0
        for i in nums:
            if i==1:
                curr +=1
            else:
                curr = 0
            max_count = max(curr,max_count)
        return max_count 
