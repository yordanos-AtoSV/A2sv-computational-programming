class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = defaultdict(list)
        for u, v in prerequisites:
            graph[v].append(u)
         
        preqmap = {}  
        def dfs(node):
            if node not in preqmap:
                preqmap[node] = set()
                
                for neigh in graph[node]:
                    preqmap[node] |= dfs(neigh)
                    
                preqmap[node].add(node)
                
            return preqmap[node]
            
            
            
        for i in range(numCourses):
            dfs(i)
            
            
        ans = []
        for u, v in queries:
            ans.append(u in preqmap[v])
            
        return ans
        