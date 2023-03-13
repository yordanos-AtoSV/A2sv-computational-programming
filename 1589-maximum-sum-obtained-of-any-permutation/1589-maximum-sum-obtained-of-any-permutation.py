class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        mod = pow(10,9) + 7
        count = [0] * (len(nums) + 1)
        for c in requests:
            count[c[0]] += 1
            count[c[1] + 1] += - 1
            
 
        count.pop()
        prefix = []
        prev = 0

        for c in count:
            prev += c
            prefix.append(prev)
            
 
        
        prefix.sort()
        nums.sort()

        sum = 0
        
        for i in range(len(nums)):
            temp = nums[i] * prefix[i]
            sum += temp
            
        return sum % mod
        