class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        for i, t in enumerate (tasks):
            t.append(i)
       
        tasks.sort(key = lambda t : t[0])
        
        
        ans, heap = [], []
        i = 0 
        t = 0
        while heap or i < len(tasks):
            while i < len(tasks) and tasks[i][0] <= t:
                heappush(heap, (tasks[i][1], tasks[i][2] ))
                i += 1
                
            if not heap:
                heappush(heap, (tasks[i][1], tasks[i][2]))
                t = tasks[i][0]
                i += 1
                         
            else:
                proct, index = heappop(heap)
                t += proct
                ans.append(index)
                
        return ans
                         
            
                         
                
        
        
        