class Solution:
    def missingNumber(self, nums: List[int]) -> int:
      
        seen = set(nums)          # store array in hashset

        for i in range(len(nums) + 1):   # 0 to n
            if i not in seen:             # check if missing
             return i
