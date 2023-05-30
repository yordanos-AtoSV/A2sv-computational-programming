class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        memo = {}
        
        def solve(n):
            temp = float("inf")
            if n == 0:
                return 0
            if n < 0:
                return inf
            if n in memo:
                return memo[n]
            
            for c in coins:
            
               temp = min(temp,  solve(n - c))
                    
            memo[n] = temp + 1
            
            return memo[n]
        
        
        ans = solve(amount)        
        return  ans if ans != inf else -1
    
    
    