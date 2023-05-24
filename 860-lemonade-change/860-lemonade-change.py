class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill5 = 0
        bill10 = 0
        for nums in bills :
            if nums == 5:
                bill5 += 1
            elif nums == 10:
                if bill5 > 0 :
                    bill10 += 1
                    bill5 -= 1
                else:
                    return False
            else:
                if bill10 > 0 and bill5 > 0:
                    bill10 -= 1
                    bill5 -= 1
                elif bill5 >= 3:
                    bill5 -= 3
                else:
                    return False
                
                
        return True
                    