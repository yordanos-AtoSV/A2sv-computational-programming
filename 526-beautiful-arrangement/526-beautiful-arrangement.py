class Solution:
    def countArrangement(self, n: int) -> int:
        path = []
        count = 0
        sets = 0
        
        def back(sets, path):
            nonlocal count
            
            if len(path) == n:
                count += 1
                return 
            for i in range(1, n + 1):
                
                temp = 1 << i
                ands = temp & sets
                if ands == 0:
                    if i % (len(path) + 1) == 0 or (len(path)+1) % i == 0:
                        path.append(i)
                        sets |= temp
                        back(sets, path)
                        path.pop()
                        sets ^= temp
                        
                else:
                    continue
                    
                    
        back(sets, path)   
        return count
        