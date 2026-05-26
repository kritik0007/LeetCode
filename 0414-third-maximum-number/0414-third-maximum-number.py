class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        largest = float('-inf')
        second = float('-inf')
        third = float('-inf')
        for num in nums:
            if num in (largest, second, third):  
                continue
            if(num>largest):
                third = second
                second = largest
                largest = num
            elif(num>second and num<largest):
                third = second 
                second = num
            elif(num>third and num<second):
                third = num
        if(third == float('-inf')):
            return largest
        elif(second == float('-inf')):
            return largest
        else:
            return third 