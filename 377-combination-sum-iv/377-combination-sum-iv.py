class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
       
        memo = defaultdict(int)
        def solve(target):
            
            if target == 0:
              
                return 1
            if target < 0:
                return 0
            j = 0
            if target not in memo:
                for n in nums:
                   
                    temp = target - n
                    j += solve(temp)
                    memo[target] = j
               
            return memo[target]
    
        x  = 0
        x += solve(target)
        return memo[target]
            