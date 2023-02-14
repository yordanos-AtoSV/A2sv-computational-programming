class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
#         l = 0 
#         r = len(nums) - 1
#         nums.sort()
#         count = 0
#         while l<r:
#             curr = nums [l] + nums[r] 
#             if curr== k:
#                 count += 1
#                 r -= 1
#                 l +=1
                
#             elif curr < k:
#                 l +=1
#             else:
#                 r -= l

          
        
#         return count
        nums.sort()
        left = 0
        right = len(nums) - 1
        ans = 0
        while left < right:
            cur = nums[left] + nums[right]
            if cur == k:
                ans += 1
                left += 1
                right -= 1
            elif cur < k:
                left += 1
            else:
                right -= 1
        
        return ans


