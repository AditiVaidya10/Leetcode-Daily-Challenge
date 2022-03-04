class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        rows = query_row + 1
        arr = [[0]*(row+1) for row in range(rows)]
        arr[0][0] = poured
        for i in range(1,rows):
            arr[i][0] = max(0,(arr[i-1][0] - 1)/2)
            arr[i][i] = max(0,(arr[i-1][i-1]-1)/2)
            for j in range(1,i):
                arr[i][j] = max(0,(arr[i-1][j-1]-1)/2)+ max(0,(arr[i-1][j]-1)/2)
        return min(arr[query_row][query_glass],1)
