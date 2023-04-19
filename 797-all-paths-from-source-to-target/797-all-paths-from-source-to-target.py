class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        adjlist = defaultdict(list)
        for i in range(len(graph)):
            for j in range(len(graph[i])):
                adjlist[i].append(graph[i][j])
                
        ans = []
        def dfs(node, path ):
            
                if node == len(graph) - 1:
                    path.append(node)
                    ans.append(path[:])
                    path.pop()
           
                path.append(node)
               
                
                for nodes in adjlist[node]:
                    dfs(nodes, path)
                    
                 
                
                path.pop()
                

        dfs(0, [])
            
        return ans    