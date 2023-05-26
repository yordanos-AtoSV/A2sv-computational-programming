class Solution:
    def rob(self, nums: List[int]) -> int:
        memo = {}
        def solve(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[1], nums[0])
            
            if i not in memo:
                memo[i] = max(solve(i -1), solve(i - 2) + nums[i])
                
                return memo[i]
            
            return memo[i]
        
        
        return solve(len(nums) - 1)