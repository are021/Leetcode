class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        #Transposing Matrix Then Reversing
        rows = cols = len(matrix)
        for r in range(rows):
            for c in range(r,cols):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]
            
        
        for r in matrix:
            r.reverse()


#Online solution (Neetcode)
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        #Boundary pointer solution

        l, r = 0, len(matrix) - 1

        while l < r :
            for i in range(r - l):
                top, bottom = l, r

                #save top left
                tmp = matrix[top][l + i]

                matrix[top][l + i] = matrix[bottom - i][l]

                matrix[bottom - i][l] = matrix[bottom][r - i]

                matrix[bottom][r - i] = matrix[top + i][r]

                matrix[top + i][r] = tmp

            r -= 1
            l += 1
        





        