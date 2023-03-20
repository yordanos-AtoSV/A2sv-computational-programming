class Solution:
    def countVowelStrings(self, n: int) -> int:
        a = 5
        self.counti = 0
        
        def back(k,i):
            if k == n:
                self.counti += 1
                return
            
            for j in range(i,a):
                back(k+1, j)
        
        for i in range(a):
            back(1,i)
        
        return self.counti