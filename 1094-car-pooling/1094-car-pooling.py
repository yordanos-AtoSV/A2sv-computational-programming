class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        passchange = [0] * 1001 
        
        for t in trips:
            numpass, start, end = t
            passchange[start] += numpass
            passchange[end] -= numpass
       
        passSum = 0
        for c in passchange:
            passSum += c
            
            if passSum > capacity:
                
                return False
            
        return True
            
           