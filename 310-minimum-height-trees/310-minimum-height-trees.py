class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        
        q = deque()
        for u in graph:
            if len(graph[u]) == 1:
                q.append(u)
    
    
        while n > 2:
 
            size = len(q) 
            n = n - size 
        
            for i in range (size):
                temp = q.popleft()
                for neigh in graph[temp]:
                    graph[neigh].remove(temp)
                    if len(graph[neigh]) == 1:
                        q.append(neigh)

        
 
        ans = []

        while q:
            ans.append(q.pop())
            
        return ans