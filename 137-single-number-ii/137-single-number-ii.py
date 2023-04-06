class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        dic = defaultdict(int)
        count = 0
        for num in nums:
            i = 0
            while num:
                if num < 0:
                    count += 1
                    num = -(num)
                temp = num & 1
                if temp == 1:
                    dic[i] += 1
                num >>= 1
                i += 1
       
        ans = 0        
        for key, item in dic.items():
            temp = (item % 3) << key
            ans |= temp
            
        if count % 3 == 0:   
            return ans   
        else:
            return - ans 
            
                
        

            