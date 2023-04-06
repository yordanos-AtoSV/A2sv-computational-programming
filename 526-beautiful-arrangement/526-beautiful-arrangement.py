class Solution:
    def countArrangement(self, n: int) -> int:
        path = []
        count = 0
        sets = set()
        
        def back(sets, path):
            nonlocal count
            if len(path) == n:
                count += 1
                return 
            for i in range(1, n + 1):
                
                if i in sets:
                    continue
                else:
                    if i % (len(path) + 1) == 0 or (len(path)+1) % i == 0:
                        path.append(i)
                        sets.add(i)
                        back(sets, path)
                        path.pop()
                        sets.remove(i)
                    
        back(sets, path)   
        return count
        