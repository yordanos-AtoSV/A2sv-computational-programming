class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        flag = False
        for row in matrix:
            if target in row:
                flag = True
        return flag
