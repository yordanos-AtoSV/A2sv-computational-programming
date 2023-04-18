class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province = 0
        visited = set()
        def dfs(start):
            visited.add(start)
            for end in range(len(isConnected)):
                if isConnected[start][end] and end not in visited:
                    dfs(end)
            
                    
        for start in range(len(isConnected)):
            if start not in visited:
                province += 1
                dfs(start)
        
        return province