class NumArray:

    def __init__(self, nums: List[int]):
        self.prefsum = [0]
        for i in range(len(nums)):
            
            self.prefsum.append(self.prefsum[- 1] + nums[i])
            
        
        

    def sumRange(self, left: int, right: int) -> int:
        
        return self.prefsum[right + 1] - self.prefsum[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)

# [-2, 0, 3, -5, 2, -1]
# [-2, -2, 1 , -4, -2, -3]