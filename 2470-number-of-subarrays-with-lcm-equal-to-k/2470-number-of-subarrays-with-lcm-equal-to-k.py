from math import gcd

class Solution:
    def subarrayLCM(self, nums, k):
        def lcm(a,b):
            return a*b // gcd(a,b)

        ans = 0
        n = len(nums)

        for i in range(n):
            cur = 1

            for j in range(i,n):

                if k % nums[j] != 0:
                    break

                cur = lcm(cur, nums[j])

                if cur == k:
                    ans += 1

                elif cur > k:
                    break

        return ans