class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        if "0000" in deadends:
            return -1
        queue = deque()
        visited = set()
        queue.append("0000")
        visited.add("0000")
        level = 0
        while queue:
            n = len(queue)
           
            for _ in range(n):
                
                s = queue.popleft()
            
                if s == target:
                    return level
                d = list(map(int, s))
           
                orig = d[:]
                for i in range(4):
                    
                    if d[i] == 9:
                        temp2 = 0
                        d[i] = temp2
                    else:
                        
                        temp2 = d[i] + 1
                        d[i]  = temp2
                   
                    
                    temp2 = "".join(map(str, d))


                    if temp2 not in deadends and temp2 not in visited:
                        queue.append(temp2)
                        visited.add(temp2)    
                    d = orig[:] 
                    
                    if d[i] == 0:
                        temp2 = 9
                        d[i] = temp2
                    else:
                        temp2 = d[i] - 1 
                        d[i] = temp2
                    
                      
                        
                        
                    temp = "".join(map(str, d))


                    if temp not in deadends and temp not in visited:
                        queue.append(temp)
                        visited.add(temp)
                        
                    d = orig[:] 
                    

            level += 1 
            
            
        return - 1