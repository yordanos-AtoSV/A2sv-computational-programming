import collections
class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        prefix = [0]
        for i in range(len(nums)):
            prefix.append(prefix[-1] + nums[i])
            
       
        sizemin = float("inf")
        queue = deque()
        queue.append([0,prefix[0]])
        
        
        for i in range(1, len(nums) + 1):
            
            while queue and queue[-1][1] > prefix[i]:
                queue.pop()
              
            
            while queue and prefix[i] - queue[0][1] >= k: 
                
    
                sizemin = min(i - queue[0][0], sizemin)
                queue.popleft()
                
             
            
                    
            queue.append([i, prefix[i]])
          
        if sizemin   == inf:
            return -1 
        return sizemin
        
        