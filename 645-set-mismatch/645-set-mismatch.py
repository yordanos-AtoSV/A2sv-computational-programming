class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        l = 0
        while l < len(nums) :
            index = nums[l] - 1
            
                
            if l != index and nums[l] != nums[index]:
                nums[l], nums[index] = nums[index], nums[l]
            else :
                l += 1
        ans = []        
        for i in range(len(nums)):
            index = nums[i] - 1
            if index != i:
                ans.append(nums[i])
                ans.append(i + 1)
                
        return ans