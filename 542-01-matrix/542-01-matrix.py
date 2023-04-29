class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        ans = [[0 for _ in range(len(mat[0]))]] * len(mat)
  
        direc = [(0,1), (1,0), (-1, 0), (0, -1)]
        inbound = lambda row, col: 0 <= row < len(mat) and 0 <= col < len(mat[0])
        queue = deque()
        visited = set()
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if mat[i][j] == 0:
                    queue.append((i, j))
                else:
                    mat[i][j] = -1
                    
        
        while queue:
            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                for r, c in direc :
                    nr= row + r
                    nc = col + c

                    if inbound(nr, nc) and mat[nr][nc] == -1:
                        mat[nr][nc] = mat[row][col] + 1
                        queue.append((nr, nc))
                    
                    
   
            
        return mat
        

        