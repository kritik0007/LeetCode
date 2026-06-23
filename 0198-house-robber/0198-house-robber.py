class Solution:
    def rob(self, nums: List[int]) -> int:
        
        prev2 = 0
        prev1 = 0

        for num in nums:
            curr = max(prev2 + num, prev1)  # rob or skip?
            prev2 = prev1                    # shift forward
            prev1 = curr                     # shift forward

        return prev1    