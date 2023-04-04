class Solution:
    def subarrayGCD(self, nums: List[int], k: int) -> int:
        def calcugcd(a, b):
            if b == 0:
                return a
            return calcugcd(b, a % b)
        
        count = 0
       
        for i in range( len(nums)):
            gcd = nums[i]
            for j in range(i, len(nums)):
                gcd = calcugcd(nums[j], gcd)
                if gcd == k:
                    count += 1
    
                
        return count
            
            
        