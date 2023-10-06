# BFS Problem
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        visit = set() #Visited Islands
        islands = 0

        def bfs(r, c):
            q = collections.deque()
            visit.add(r, c)
            q.append((r,c))

            while q:
                row, col = q.popleft()
                #Check adjacent positions of popped item
                directions = [(1,0), (-1,0), (0, 1), (0, -1)] #Loop through adjacents

                for dx, dy in directions:
                    r, c = row + dx, col + dy
                    if ((r) in range(rows) and (c) in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.append((r, c))


        for r in range(rows):

            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    bfs(r, c)
                    islands += 1

        return islands

# DFS Solution
class Solution:
    def dfs(self, grid, r , c, rows, cols):
        if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] != '1':
            return

        grid[r][c] = "0"
        # 4 recursive bfs calls
        self.dfs(grid, r + 1, c)
        self.dfs(grid, r - 1, c)
        self.dfs(grid, r, c + 1)
        self.dfs(grid, r, c - 1)


    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        
        rows, cols = len(grid), len(grid[0])
        islands = 0
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    islands += 1
