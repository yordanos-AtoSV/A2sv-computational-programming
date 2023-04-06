class Solution:
    def minSteps(self, n: int) -> int:
        factors = []
        
        d = 2
        while 2*2 <= n:
            while n % d == 0:
                factors.append(d)
                n //= d
                    
            d += 1
                
        if n > 1:
            factors.append(n)
            
        return sum(factors)    
        
