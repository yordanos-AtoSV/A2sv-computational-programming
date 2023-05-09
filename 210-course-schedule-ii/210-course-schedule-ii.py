class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        for num1, num2 in prerequisites:
            graph[num2].append(num1)
            incoming[num1] += 1
       
        q = deque() 
        ans = []
        for i in range(len(incoming)):
            if incoming[i] == 0:
                q.append(i)
                
        while q:
            temp = q.popleft()
            ans.append(temp)
            
            
            for neigh in graph[temp]:
                
                incoming[neigh] -= 1
                if incoming[neigh] == 0:
                    q.append(neigh)
                    
        if len(ans) != numCourses:
            return []
        
        
        return ans
                
            
            
            