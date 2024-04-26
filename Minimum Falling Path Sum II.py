class Solution:
    def minFallingPathSum(self, grid: List[List[int]]) -> int:
        n = len(grid)
        m = len(grid[0])
        res = float('inf')
        dp = [[-1] * m for _ in range(n)]

        for j in range(m):
            dp[0][j] = grid[0][j]

        for i in range(1, n):
            for j in range(m):
                temp = float('inf')

                for k in range(m):
                    if j != k:
                        temp = min(temp, grid[i][j] + dp[i - 1][k])

                dp[i][j] = temp

        for j in range(m):
            res = min(res, dp[n - 1][j])

        return res
