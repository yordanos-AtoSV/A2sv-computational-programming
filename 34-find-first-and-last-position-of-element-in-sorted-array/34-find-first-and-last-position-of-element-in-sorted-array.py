class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]
        left = self.serch(nums, target, True)
        right = self.serch(nums, target, False)
        
        return [left, right]
        
        
    def serch(self, nums: List[int], target: int, turn:bool) -> int :
        best = -1  
        l = -1 
        r = len(nums)
         
        while l + 1 < r:
            
            mid = l + (r - l) // 2
            
            if turn:
                
                if nums[mid] < target :
                    l = mid
                else :
                    r = mid
                    best = mid
            
            else :
               
                if nums[mid] > target:
                    r = mid
                else :
                    l = mid
                    best = mid
        
        if nums[best] == target:
            
            return best
        else:
            return -1
        
            
            

                    
            
            
        
        
    
         
        