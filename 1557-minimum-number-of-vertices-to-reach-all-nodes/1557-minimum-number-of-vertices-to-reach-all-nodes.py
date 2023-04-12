class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        
        for num in edges:
            graph[num[1]].append(num[0])
          
       
       
        ans = []
        for i in range(n):
            if len(graph[i]) == 0:
                ans.append(i)
                
                
        return ans        
    
                
            