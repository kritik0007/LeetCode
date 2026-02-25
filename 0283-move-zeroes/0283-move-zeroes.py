class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        insert_pos = 0
        
        # Move non-zero elements forward
        for num in nums:
            if num != 0:
                nums[insert_pos] = num
                insert_pos += 1
        
        # Fill remaining positions with zero
        for i in range(insert_pos, len(nums)):
            nums[i] = 0