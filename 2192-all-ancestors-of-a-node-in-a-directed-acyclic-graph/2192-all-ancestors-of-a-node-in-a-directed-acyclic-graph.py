class Solution:
    def getAncestors(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        indegree = defaultdict(int)
        
        for edge1, edge2 in edges:
            graph[edge1].append(edge2)
            if edge1 not in indegree:
                indegree[edge1] = 0
            indegree[edge2] += 1
            
        
        q = deque()
        for key in indegree:
            if indegree[key]  == 0:
                q.append(key)
               
        ans = [set() for _ in range(n)]
        
        
        while q:
            temp = q.popleft()
            
            for neigh in graph[temp]:
                indegree[neigh] -= 1
                if indegree[neigh] == 0:
                    q.append(neigh)
                    
                ans[neigh].add(temp)
                if ans[temp]:
                    for nums in ans[temp]:
                        ans[neigh].add(nums)
               
        for i in range(len(ans)):
     
            ans[i] = list(ans[i])
            ans[i].sort()
        
        return ans
        
        