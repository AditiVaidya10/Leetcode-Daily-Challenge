class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        countRow = []
        for rowIdx, row in enumerate(mat):
            count = sum(row)
            countRow.append([rowIdx, count])
        countRow.sort(key = lambda x: x[1])
        res = [0] * k
        for i in range(k):
            res[i] = countRow[i][0]    
        return res
