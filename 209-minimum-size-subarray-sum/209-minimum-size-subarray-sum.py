class Solution:
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        ans = math.inf
        cur_sum = 0
        j = 0

        for i, num in enumerate(nums):
              cur_sum += num
              while cur_sum >= s:
                ans = min(ans, i - j + 1)
                cur_sum -= nums[j]
                j += 1
                
        return ans if ans != math.inf else 0
