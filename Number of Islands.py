class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ans = 0
        def finding(i,j):
            grid[i][j] = '0'
            #upwards:
            if i-1 >= 0 and grid[i-1][j] == '1':
                finding(i-1,j)
            #downwards
            if i+1 <= len(grid)-1 and grid[i+1][j] == '1':
                finding(i+1,j)
            #rightwards
            if j+1 <= len(grid[0])-1 and grid[i][j+1] == '1':
                finding(i,j+1)
            #leftwards
            if j-1 >= 0 and grid[i][j-1] == '1':
                finding(i,j-1)
    
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]=='1':
                    ans+=1
                    finding(i,j)
        return ans
