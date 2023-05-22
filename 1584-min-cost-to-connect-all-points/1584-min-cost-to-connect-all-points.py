class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        graph = defaultdict(list)
        for i in range(n):
            x1, y1 = points[i]
            for j in range(i + 1, n):
                x2, y2 = points[j]
                cost = abs(x2 - x1) + abs(y2 - y1)
                graph[i].append((cost, j))
                graph[j].append((cost, i))
         
 
        heap = [(0, 0)]
        visited = set()
        res = 0
        
        while len(visited) < n:
            
            cost, node = heappop(heap)
            if node not in visited:
                visited.add(node)
                res += cost
                for cst , neig in graph[node]:
                        if neig not in visited:
                            heappush(heap, (cst, neig))
            
        return res