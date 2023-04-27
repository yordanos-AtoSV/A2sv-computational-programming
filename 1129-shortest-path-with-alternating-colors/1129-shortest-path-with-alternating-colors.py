class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for i , j in redEdges:
            graph[i].append((j, 1))
            
        for i , j in blueEdges:
            graph[i].append((j, 2))
            
            
        queue = deque()
        visited = set()
        answer = [-1] * n
        queue.append((0, None))
        visited.add((0, None))
        level = 0
        while queue :
                n = len(queue)
                
                for i in range(n):
                    node, prev = queue.popleft()
                    if answer[node] == -1:
                        answer[node] = level
                    
                    for neigh, col in graph[node]:
                        if prev != col and (neigh, col) not in visited:
                            queue.append((neigh, col))
                            visited.add((neigh, col))
                            
                level += 1
                
                
                
        return answer
                            
                    
        
        