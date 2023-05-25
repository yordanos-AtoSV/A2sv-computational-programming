class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        x, y = float("inf"), float("inf")
        for num in nums:
            if num <= x:
                x = num
            elif num <= y:
                y = num
            else:
                return True 
            
        return False