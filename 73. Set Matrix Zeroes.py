class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    print(i,j)
                    for k in range(len(matrix)):
                        for m in range(len(matrix[0])):
                            if matrix [i][m] != 0:
                                matrix[i][m] = '0'
                        if matrix[k][j] != 0:
                            matrix[k][j] = '0'
        
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                matrix [i][j] = int (matrix[i][j])
        return matrix
