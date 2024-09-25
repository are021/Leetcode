class Solution:

    def isEdge(self, board, r, c, m, n):
        if r >= m or c >= n or c < 0 or r < 0:
            return True
        return False

            

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        
        m, n = len(board), len(board[0])

        def dfs(board, r, c, m, n):
            if self.isEdge(board, r, c, m, n) or board[r][c] != "O":
                return
            
            board[r][c] = "T" #Temp character
            dfs(board, r + 1, c, m, n)
            dfs(board, r - 1, c, m, n)
            dfs(board, r, c - 1, m , n)
            dfs(board, r, c + 1, m, n)

        # col check
        for r in range(m):
            if board[r][0] == "O": 
                dfs(board, r, 0, m, n)
            if board[r][n - 1] == "O":
                dfs(board, r, n - 1, m, n)
        
        for c in range(n):
            if board[0][c] == "O":
                dfs(board, 0, c, m, n)
            if board[m - 1][c] == "O":
                dfs(board, m - 1, c, m, n)
        

        # Now change all remaining o's to X

        for r in range(m):
            for c in range(n):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "T":
                    board[r][c] = "O"
                         

        




