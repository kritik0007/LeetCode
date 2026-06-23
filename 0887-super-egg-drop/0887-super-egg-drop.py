class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        
    # dp[m][k] = max floors we can check
    # with m moves and k eggs
        dp = [[0] * (k+1) for _ in range(n+1)]
        m = 0  # moves counter

        while dp[m][k] < n:
         m += 1
         for j in range(1, k+1):
            dp[m][j] = dp[m-1][j-1] + dp[m-1][j] + 1

        return m