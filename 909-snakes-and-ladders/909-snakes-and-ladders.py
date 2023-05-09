class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        board.reverse()
        def giverandc(square):
            r = (square - 1) // n
            c = (square - 1) % n
            
            if r % 2:
                c = n - 1 - c
                
            return [r, c]
            
        q = deque()
        visited = set()
        q.append([1, 0])
        
        while q:
            square, move = q.popleft()
            
            for i in range(1, 7):
                nextsquare = i + square
                row, col = giverandc(nextsquare)
                if board[row][col] != -1:
                    nextsquare = board[row][col]
                if nextsquare == n * n:
                    return move + 1
                if nextsquare not in visited:
                    visited.add(nextsquare)
                    q.append([nextsquare, move + 1])
                    
                    
        return - 1
                
                
            
            