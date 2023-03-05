class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefixsumCount = {0:1}
        ans = 0
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            diff = sum - k 
            if diff in prefixsumCount:
            
                ans += prefixsumCount[diff]
          
            if sum not in prefixsumCount:
                prefixsumCount[sum] = 1
            else:
                prefixsumCount[sum] += 1
                
                
        return ans
            
            
        