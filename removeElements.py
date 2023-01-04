class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val in nums:
            nums.remove(val)
        return len(nums)
        # count=0
        # for i in range(len(nums)):
        #     if nums[i]==val:
        #         nums[i]="_"
        #         count+=1
        # print(len(nums)-count)
        # i=len(nums)-1
        # j=0
        # print(nums)

        # while i==j:
        #     if (nums[j]=="_"):
                
        #         nums[j],nums[i]=nums[i],nums[j]
        #         j+=1
        #         i-=1
        #     else:
        #         j+=1
        # return


    
    
