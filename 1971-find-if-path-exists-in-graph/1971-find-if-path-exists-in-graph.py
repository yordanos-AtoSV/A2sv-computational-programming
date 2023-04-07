class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        adjlist = defaultdict(list)
        
        for edge in edges:
            adjlist[edge[0]].append(edge[1]) 
            adjlist[edge[1]].append(edge[0])
            
        
        visited  = set()
        def recur(node, visited):
            if node == destination:
                return True
            
            visited.add(node)
            
            for neigh in adjlist[node]:
                if neigh not in visited:
                    found = recur(neigh, visited)
                    
                    if found :
                        return True
                
            return False    
            
        return recur(source, visited)