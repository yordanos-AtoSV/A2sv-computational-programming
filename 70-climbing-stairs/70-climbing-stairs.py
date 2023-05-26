class Solution:
    def climbStairs(self, n: int) -> int:
        memo = {}
        def solve(n):
            if n == 1:
                return 1
            if n == 0:
                return 1
            
            if n not in memo:
                memo[n] = solve(n - 1) + solve(n - 2)
                return memo[n]
            return memo[n]
        
        return solve(n)
            