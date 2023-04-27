class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
      
        queue = deque()
        visited = set()
        visited.add(0)
        for num in rooms[0]:
            queue.append(num)
        
        while queue:
            key = queue.popleft()
            
            if key not in visited and key not in queue:
                visited.add(key)
                
            for num in rooms[key]:
                if num not in visited and num not in queue:
                    queue.append(num)
                    
                    
        return len(visited) == len(rooms)
            
            