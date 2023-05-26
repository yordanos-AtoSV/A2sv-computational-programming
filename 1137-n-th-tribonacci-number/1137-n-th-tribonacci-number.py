class Solution:
    def tribonacci(self, n: int) -> int:
        memo = {}
        
        def solve(n):
            if n == 1 or n == 2:
                return 1
            if n == 0:
                return 0
            
            if n not in memo:
                memo[n] = solve(n - 1) + solve(n - 2) + solve(n - 3)
                return memo[n]
            
            return memo[n]
        
        return solve(n)
        