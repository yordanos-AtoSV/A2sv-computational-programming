class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        size = len(nums)
        temp = (2 ** size)
        
        for i in range(temp):
            count = 0
            w = []
            while i != 0:
                temp2 = i & 1
                if temp2 == 1:
                    w.append(nums[(len(nums) - count) - 1])
                    
                i = i >> 1
                count += 1
                
            ans.append(w)
            
        return ans
                
        