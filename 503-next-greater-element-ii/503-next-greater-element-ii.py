class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1] * len(nums)
        stack = []
        n = len(nums)
        for i in range((2 * n)):
            while stack and nums[stack[-1]] < nums[i % n ]:
                temp = stack.pop()
                ans[temp] = nums[i % n]
                
            stack.append(i % n)
            
        return ans 
                       