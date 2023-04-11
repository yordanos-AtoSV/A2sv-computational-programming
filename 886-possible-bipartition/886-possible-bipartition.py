class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        
        for a, b in dislikes:
            graph[a].append(b)
            graph[b].append(a)
        
        colors = [-1] * (n + 1)
        
        def dfs(node, parent, colors):
            
            if parent == -1:
                colors[node] = "a"
            else:
                if colors[node]  != -1:
                    return not (colors[node] == colors[parent])
                
                if colors[parent] == "a":
                    colors[node] = "b"
                else:
                    colors[node] = "a"
                    
            
            for neigh in graph[node]:
                
                val = dfs(neigh, node, colors)
                if not val:
                    return False
            
            return True
        
        for i in range(1, n + 1):
            if colors[i] == -1:
                val = dfs(i, -1, colors)
                if not val:
                    return False
        return True         
                
                
        