class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
        ans = []
        visited = set()
        def dfs(node):
            visited.add(node)
            ans.append(node)
            for neigh in graph[node]:
                if neigh not in visited:
                    
                    dfs(neigh)
            
        for u in graph:
            if len(graph[u]) == 1:
                if u not in visited:
                    dfs(u)
                
        return ans
            
            