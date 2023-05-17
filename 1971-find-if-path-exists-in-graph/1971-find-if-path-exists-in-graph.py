class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if destination == source:
            return True
        
        adjlist = defaultdict(list)
        
        for edge in edges:
            adjlist[edge[0]].append(edge[1]) 
            adjlist[edge[1]].append(edge[0])
            
        
        visited  = set()
        stack = []
        stack.append(source)
        
        while stack:
            cur = stack.pop()

            for neigh in adjlist[cur]:

                if neigh not in visited :
                    visited.add(neigh)
                    stack.append(neigh)

        if destination in visited:
            return True
            
        return False