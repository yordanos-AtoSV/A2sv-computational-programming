class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
 
        counter = defaultdict(int)
        l = 0 
        
        for r in range(len(fruits)):
            counter[fruits[r]]  += 1
            if len(counter) > 2:
                counter[fruits[l]] -= 1
                if counter[fruits[l]] == 0:
                    del counter[fruits[l]]
                l += 1
                
                
        return r - l + 1
            
            
             
            
        