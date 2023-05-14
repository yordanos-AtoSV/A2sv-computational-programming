from typing import List
from collections import deque
from collections import defaultdict
class Solution:
    #Function to detect cycle in an undirected graph.
	def isCycle(self, V: int, adj: List[List[int]]) -> bool:
		
        visited = set()
        def dfs(node, parent):
            
            for neigh in adj[node]:
                if neigh != parent:
                    if neigh in visited:
                        return True
                    else:
                        visited.add(neigh)
                        if dfs(neigh, node):
                            return True 
                
                    
            return False        
                        
            
                
        
		             
	    for i in range(v):
	        if i not in visited:
	            visited.add(i)
    	        if dfs(i, None):
    	            return True
    	            
        return False
	        


#{ 
 # Driver Code Starts
if __name__ == '__main__':

	T=int(input())
	for i in range(T):
		V, E = map(int, input().split())
		adj = [[] for i in range(V)]
		for _ in range(E):
			u, v = map(int, input().split())
			adj[u].append(v)
			adj[v].append(u)
		obj = Solution()
		ans = obj.isCycle(V, adj)
		if(ans):
			print("1")
		else:
			print("0")

# } Driver Code Ends
