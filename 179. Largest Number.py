class Solution:
    def largestNumber(self, nums: List[int]) -> str:
            
            for i in range(len(nums)):
                for j in range (len(nums) - 1):

                    s1 = str(nums[j]) + str(nums[j+1])
                    s2 = str(nums[j+1]) +  str(nums[j]) 
                    
                    s1, s2 = int(s1) ,int(s2)
                    if s2 > s1:
                        nums[j], nums[j + 1] = nums[j + 1], nums[j]
         
            ans = "".join(map(str, nums))
            if ans[0] == "0":
                return "0"
            return ans
