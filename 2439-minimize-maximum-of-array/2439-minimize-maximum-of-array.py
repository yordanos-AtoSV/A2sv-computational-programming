class Solution:
    def minimizeArrayValue(self, nums: List[int]) -> int:
        prefix, maxim = nums[0], nums[0]
        
        for i in range(1, len(nums)):
            prefix += nums[i] 
            maxim = max(maxim, math.ceil(prefix / (i + 1)))
            
            
        return maxim