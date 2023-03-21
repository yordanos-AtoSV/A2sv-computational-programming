class Solution(object):
    def find132pattern(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        stack = []
        minim = nums[0]
        
        for c in nums[1:]:
            while stack and c >= stack[-1][0]:
                stack.pop()
                
            if stack and c > stack[-1][1]:
                return True
            
            stack.append([c, minim])
            minim = min(c, minim)
         
            
            
        return False