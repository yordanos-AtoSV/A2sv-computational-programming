class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l = 0
        r = int(c ** 0.5)
        
        sum = 0 
        
#         if c == 0 or c== 1:
#             return True
        while l <= r:
            sum = l ** 2 + r ** 2
            if sum == c:
                return True
            elif sum > c:
                r -= 1
            else:
                l += 1
        return False        
                
                
                
        
        