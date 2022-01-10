class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dp(row,col1,col2):
            if row==m:
                return 0
            cherries=grid[row][col1]+(0 if col1==col2 else grid[row][col2])
            ans=0
            for i in range(-1,2):
                for j in range(-1,2):
                    new_col1=col1+i
                    new_col2=col2+j
                    if 0<=new_col1<n and 0<=new_col2<n:
                        ans=max(ans,dp(row+1,new_col1,new_col2))
            return cherries+ans
        m=len(grid)
        n=len(grid[0])
        return dp(0,0,n-1)
