class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        forward =[]
        backward = []
        prev = 0
        for i in range(len(nums)):
            prev += nums[i]
            forward.append(prev)
            
        prev = 0

        for i in range(len(nums) - 1, -1, -1):
            prev += nums[i]
            backward.append(prev)
            
 
        backward.reverse()
   
        
        for i in range(len(nums)):
            if forward[i] == backward[i]:
                    return i 
        return - 1
            
            
        
            
        
        
        
# [1,7,3,6,5,6]
# [1, 8, 11 ,17, 22,28 ]
# [6, 11, 17, 20, 27,28]
# [28, 27, 20, 17, 11, 6]