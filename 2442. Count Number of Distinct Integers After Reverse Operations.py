class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
 
        def reverse(n):
            result = 0
            while n:
                result = result*10 + n%10
                n //= 10
            return result


        A = set()
        for i in range(len(nums)):
            A.add(reverse(nums[i]))
            A.add(nums[i])
        return(len(A))
        
        # return len({y for x in nums for y in (x, reverse(x))})


