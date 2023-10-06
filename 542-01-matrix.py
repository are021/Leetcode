class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0]) 
        res = [[float('inf') for i in range(cols)] for j in range(rows)]
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == 0:
                    res[i][j] = 0
                    continue
                # 4 adjacent corners
                val = float('inf')
                #Top of Matrix
                if (j - 1) >= 0 and res[i][j - 1] != float('inf'):
                    val = min(val, 1 + res[i][j - 1])

                if (j + 1) < cols and res[i][j + 1] != float('inf'):
                    val = min(val, 1 + res[i][j + 1])

                if (i - 1) >= 0 and res[i - 1][j] != float('inf'):
                    val = min(val, 1 + res[i - 1][j])

                if (i + 1) < rows and res[i + 1][j] != float('inf'):
                    val = min(val, 1 + res[i + 1][j])

                res[i][j] = val

                #Now replace the adjacent values
                if (j - 1) >= 0 and res[i][j - 1] != float('inf'):
                    res[i][j - 1] = min(res[i][j - 1], 1 + val)

                if (j + 1) < cols and res[i][j + 1] != float('inf'):
                    res[i][j + 1] = min(res[i][j + 1], 1 + val)

                if (i - 1) >= 0 and res[i - 1][j] != float('inf'):
                    res[i - 1][j] = min(res[i - 1][j], 1 + val)

                if (i + 1) < rows and res[i + 1][j] != float('inf'):
                    res[i + 1][j] = min(res[i + 1][j], 1 + val)

        return res
    
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        if not mat or not mat[0]:
            return []
        
        height, width = len(mat), len(mat[0])
        q = deque()
        MAX_VALUE = width * height

        #Initialize queue with all zeroes and set cells with 1s to maxvalue

        for i in range(height):
            for j in range(width):
                if mat[i][j] == 0:
                    q.append((i, j))
                else:
                    mat[i][j] = MAX_VALUE
        directions = [(1,0), (-1,0), (0,1), (0, -1)]

        while q:
            row, col = q.popleft()

            for dr, dc in directions:
                r, c = row + dr, col + dc
                if 0 <= r < height and 0 <= c < width and mat[r][c] > mat[row][col] + 1:
                    q.append((r,c))
                    mat[r][c] = mat[row][col] + 1
        return mat
