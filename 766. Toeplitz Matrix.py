class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        from collections import defaultdict
        diagons=defaultdict(list)
        flag = True

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):

                if diagons [i - j] != [matrix[i][j]]:
                    diagons[i-j].append( matrix [i][j])
                    
        for key in diagons:
            if len(diagons[key]) > 1:
                flag = False
          
        return flag
                                                                                
