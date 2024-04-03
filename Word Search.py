def exist(board, word):
    def backtrack(i, j, idx):
        # If we have found all characters in the word
        if idx == len(word):
            return True
        
        # Check if current position is out of bounds or doesn't match the current character
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or board[i][j] != word[idx]:
            return False
        
        # Mark the current cell as visited
        temp, board[i][j] = board[i][j], '#'
        
        # Explore adjacent cells
        found = (backtrack(i+1, j, idx+1) or
                 backtrack(i-1, j, idx+1) or
                 backtrack(i, j+1, idx+1) or
                 backtrack(i, j-1, idx+1))
        
        # Restore the original value of the current cell
        board[i][j] = temp
        
        return found

    # Iterate through the entire board to find the starting point for the word
    for i in range(len(board)):
        for j in range(len(board[0])):
            if backtrack(i, j, 0):
                return True
                
    return False
