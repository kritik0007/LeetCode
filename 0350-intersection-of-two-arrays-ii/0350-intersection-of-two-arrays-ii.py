class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = {}
        res = []
        for i in nums1:
            count[i] = count.get(i,0)+1
        for j in nums2:
            if j in count and count[j] > 0:
                res.append(j)
                count[j] -= 1
        return res 

