class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        ans = []
        dic = defaultdict(bool)
        
        def dfs(node):
            if node in dic:
                return dic[node]
            
            dic[node] = False
            
            for neigh in graph[node]:
                if not dfs(neigh):
                    return dic[node]
                
            dic[node] = True
            return dic[node]
        
        
        
        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
                
                
        return ans 