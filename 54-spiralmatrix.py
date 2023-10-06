# My Solution

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        spiralMatrix = []

        if not matrix or (len(matrix) == 0):
            return spiralMatrix

        


        # direction = ['r', 'd', 'l', 'u'] #Array to represent directions

        rowSize = len(matrix)
        colSize = len(matrix[0])

        i = 0
        j = 0
        matrix_ptr = 0 % 4

        while len(spiralMatrix) < rowSize * colSize :
            if matrix[i][j] != 101:
                spiralMatrix.append(matrix[i][j])
                matrix[i][j] = 101 #Mark the matrix

            if (matrix_ptr == 0):
                j += 1
                if j >= colSize or matrix[i][j] == 101:
                    j -= 1
                    matrix_ptr = (matrix_ptr + 1) % 4
                    
            
            if (matrix_ptr == 1):
                i += 1
                if i >= rowSize or matrix[i][j] == 101:
                    i -= 1
                    matrix_ptr = (matrix_ptr + 1) % 4

            
            if (matrix_ptr == 2):
                j -= 1

                if j < 0 or matrix[i][j] == 101:
                    j += 1
                    matrix_ptr = (matrix_ptr + 1) % 4
            
            if (matrix_ptr == 3):
                i -= 1

                if i < 0 or matrix[i][j] == 101:
                    i += 1
                    matrix_ptr = (matrix_ptr + 1) % 4
        return spiralMatrix


# Neetcode Solution
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:    
        #O (m * n), O(1)
        res = []

        left, right = 0, len(matrix[0])
        top, bottom = 0, len(matrix)


        while left < right and top < bottom : 
            #get every i in the top row

            for i in range(left, right):
                res.append(matrix[top][i])
            top += 1

            # do the right column

            for i in range(top, bottom):
                res.append(matrix[i][right-1])
            right -= 1

            #Program can be finished here if our matrix has particular structure
            
            if not (left < right and top < bottom):
                break

            # do the bottom row

            for i in range(right - 1, left - 1, -1):
                res.append(matrix[bottom - 1][i])
            bottom -= 1

            # do the left column

            for i in range(bottom - 1, top - 1, -1):
                res.append(matrix[i][left])

            left += 1
        return res


