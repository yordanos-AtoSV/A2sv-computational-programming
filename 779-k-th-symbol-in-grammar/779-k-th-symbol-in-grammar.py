class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        def recur(n, k):
            if n == 1:
                return 0
            
            mid = pow(2, n -1 ) // 2
            
            if k > mid:
                return int(not recur(n-1, k - mid))
            
            else:
                return recur(n - 1, k)
                 
                
        return recur(n, k)
                
