class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        longestSubSequence = defaultdict(int)
        
        for num in arr:
            prev = num - difference
            
            longestSubSequence[num] = 1 +  longestSubSequence[prev]
            
        return max(longestSubSequence.values())
            
          
        