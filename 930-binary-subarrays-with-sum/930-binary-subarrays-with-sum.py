class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        prefix = []
        prev = 0
        for c in nums:
            prev += c
            prefix.append(prev)
            
        dic = defaultdict(int)
        dic[0] = 1
        ans = 0 
        for c in prefix:
            diff = c - goal
            if diff in dic:
                ans += dic[diff]
            
            dic[c] += 1
                
        return ans
                