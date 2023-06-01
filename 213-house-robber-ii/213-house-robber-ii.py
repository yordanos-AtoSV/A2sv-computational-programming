class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        memo = {}
        memo2 = {}
        num1 = nums[::]
        nums = num1[1:]
        nums2 = num1[:len(nums)]

        
        def solve(i):
            if i == 0:
                return nums[i]
            if i == 1:
                return max(nums[1], nums[0])

            if i not in memo:
                memo[i] = max(solve(i -1), solve(i - 2) + nums[i])
                
            return memo[i]
        
        
        def solve2(i):
            if i == 0:
                return nums2[i]
            if i == 1:
                return max(nums2[1], nums2[0])

            if i not in memo2:
                memo2[i] = max(solve2(i -1), solve2(i - 2) + nums2[i])
      
            return memo2[i]
        
        temp1 = solve(len(nums) -1)

        temp2 = solve2(len(nums2) -1)

        return max(temp1, temp2)