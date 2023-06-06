class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        memo = {}
        
        def dp(i):
            if i > len(questions) - 1:
                return 0
            
            points, brainpower = questions[i]
            if i not in memo:
                memo[i] = max(dp(i + brainpower + 1) + points, dp(i + 1) )
               
            return memo[i]
        
        dp(0)
        return max(memo.values())