class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        maxor = 0
        for num in nums:
            maxor |= num
            
        count = 0
        def sub_set_sum(size,  sub_set_sum):
            nonlocal count 
            for i in range(size+1):
                for my_sub_set in combinations(nums, i):

                    ors = 0
                    for num in my_sub_set:
                        ors |= num

                    if ors == sub_set_sum:
                        count += 1
                                
        sub_set_sum(len(nums) , maxor)
                
        
        return count
        