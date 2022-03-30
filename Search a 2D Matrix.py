class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix)
        for row in range(n):
            if target <= matrix[row][-1]: break
        if row == n: return False
        for val in matrix[row]:
            if val == target: return True
        return False 
