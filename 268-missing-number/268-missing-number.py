class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        size = len(nums)
        num = 0
        temp = 0
        for i in range(size):
            temp ^= num ^ nums[i]
            num += 1
            
        temp = num ^ temp
        return temp
            
        
            