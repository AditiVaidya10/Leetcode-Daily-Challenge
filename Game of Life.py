class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        changes = []
        rows = len(board)
        cols = len(board[0])
        for i in range(rows):
            for j in range(cols):
                ones = 0
                if i - 1 >= 0:
                    if board[i - 1][j] == 1:
                        ones += 1
                    if j - 1 >= 0:
                        if board[i - 1][j - 1] == 1:
                            ones += 1
                    if j + 1 < cols:
                        if board[i - 1][j + 1] == 1:
                            ones += 1
                if i + 1 < rows:
                    if board[i + 1][j] == 1:
                        ones += 1
                    if j - 1 >= 0:
                        if board[i + 1][j - 1] == 1:
                            ones += 1
                    if j + 1 < cols :
                        if board[i + 1][j + 1] == 1:
                            ones += 1
                if j - 1 >= 0:
                    if board[i][j - 1] == 1:
                        ones += 1
                if j + 1 < cols:
                    if board[i][j + 1] == 1:
                        ones += 1
                
                if board[i][j] == 1:
                    if ones < 2 :
                        changes.append([i,j])
                    if ones > 3:
                        changes.append([i,j])
                else:
                    if ones == 3:
                        changes.append([i,j])
        for k in changes:
            if board[k[0]][k[1]] == 1:
                board[k[0]][k[1]] = 0
            else:
                board[k[0]][k[1]] = 1
