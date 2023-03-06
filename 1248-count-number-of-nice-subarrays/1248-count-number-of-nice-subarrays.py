class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        for i in range(len(nums)):
            if nums[i] % 2 == 0:
                nums[i] = 0
            else:
                nums[i] = 1
        
 
        ans = 0
        cur_sum = 0
        prefMap = {0:1}
        
        
        for i in range(len(nums)):
            
            cur_sum += nums[i]
            
            diff = cur_sum - k
           
            if diff in prefMap:
                ans += prefMap[diff]
            
            prefMap[cur_sum] = 1 + prefMap.get(cur_sum, 0)
            
            
        return ans
      