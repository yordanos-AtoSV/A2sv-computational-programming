class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = set()
        temp = []
        
        def backtrack(idx):
            if idx == len(nums):
                if len(temp) >= 2:
                    ans.add(tuple(temp))
                return 
            if not temp or temp[-1] <= nums[idx]:
                temp.append(nums[idx])
                backtrack(idx + 1)
                temp.pop()
                
            backtrack(idx + 1)
            
        backtrack(0)
        return ans
        
                    
            