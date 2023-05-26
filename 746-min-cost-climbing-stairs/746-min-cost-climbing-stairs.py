class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        memo = {}
        n = len(cost)
        if n == 2:
            return min(cost)
        cost.append(0)
        def solve(i):
            if i >= n - 1:
                return cost[i]
            
            if i not in memo:
                memo[i] = cost[i] + min(solve(i + 1), solve(i + 2))
                return memo[i]
            return memo[i]
        
        solve(0)
        print(memo[0])
        return min(memo[0], memo[1])