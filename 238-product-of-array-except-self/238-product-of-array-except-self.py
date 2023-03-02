class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
     
        forward = [1]
        for i in range(len(nums)):
             forward.append(forward[-1] * nums[i] )
                
        backward = [1]
        for i in range(len(nums) - 1, -1 , -1):
            
            backward.append(backward[-1] * nums[i])
            
        backward.reverse()
        
        print(forward)
        print(backward)
        ans = []
        
        for i in range(1,len(backward)):
            left = forward[i -1]
            right = backward[i]
            ans.append(left * right)
        
        
        return ans
        

            