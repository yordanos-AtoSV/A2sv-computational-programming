class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        i = 0
        ptr1 = 0 
        ptr2 = 1
        while i< len(nums) - 1:

            if nums[ptr1] == nums[ptr2]:
        
                nums[ptr2] = "_"
                ptr2 += 1
            
            else:

                ptr1 = ptr2
                ptr2 += 1
              
            
            i += 1
       

        holder = 0
        seeker = 0

        while seeker < len(nums):

            if nums[seeker] != "_":
                nums[holder], nums[seeker] = nums[seeker], nums[holder]
                holder += 1
            seeker += 1
    
        count = 0
        for i in range(len(nums)):
            if nums[i] != "_":
                count += 1
        
        return count


