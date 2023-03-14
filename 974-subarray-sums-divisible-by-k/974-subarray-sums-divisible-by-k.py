class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prev = 0
        count = defaultdict(int)
        count[0] = 1
        ans = 0
        for c in nums:
            prev += c
            dif = prev % k 
            ans += count[dif]
            count[dif] += 1
            
        return ans
        
