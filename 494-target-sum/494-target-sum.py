class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = {}
        
        def solve(idx, tot):
            if idx == len(nums):
                if tot == target:
                    return 1
                else:
                    return 0
            if (idx, tot)not in dp:    
                dp[(idx, tot)] = solve(idx + 1, tot + nums[idx]) + solve(idx + 1, tot - nums[idx])
            else:
                return dp[(idx, tot)]
            
            
            return dp[(idx, tot)]
                                       
                                       
        return solve(0, 0)