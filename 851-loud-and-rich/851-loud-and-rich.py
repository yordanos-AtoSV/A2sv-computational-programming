class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        ans = [None for _ in range(n)]
        graph = defaultdict(list)
        
        for u, v in richer:
            graph[v].append(u)
            
        for i in range(n):
            if not graph[i]:
                graph[i] = []
        
        def dfs(node):
            if ans[node]:
                return ans[node]
            if not graph[node]:
                return node
            
            minim = node
            for neigh in graph[node]:
                temp = dfs(neigh)
                if quiet[temp] < quiet[minim]:
                    minim = temp
                    
            ans[node] = minim
            return minim
        
        for i in range(n):
            if not ans[i]:
                ans[i] = dfs(i)
                
        return ans