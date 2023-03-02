class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        forward =[0]

        for i in range(len(nums)):
            forward.append(forward[-1] + nums[i])
            

        for i in range(1, len(forward)):
            left_sum = forward[i -1]

            right_sum =forward[len(forward) - 1] - forward[i]
  
            if right_sum == left_sum:
                return i - 1
            
        return -1 
            
            

            
            
        
            
        
        
        
# [1,7,3,6,5,6]
# [1, 8, 11 ,17, 22,28 ]
# [6, 11, 17, 20, 27,28]
# [28, 27, 20, 17, 11, 6]