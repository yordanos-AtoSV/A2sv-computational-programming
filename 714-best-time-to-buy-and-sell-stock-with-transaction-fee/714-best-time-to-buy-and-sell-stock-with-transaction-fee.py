class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        memo = {}
        
        def dp(idx, d_s):
            
            if idx > len(prices) - 1:
                return 0

            
            if (idx, d_s) not in memo:
                if d_s == 1:
                    v1 = dp(idx + 1, 1) 
                    v2 = dp(idx + 1, 2) - fee - prices[idx]
                   
                    memo[(idx, d_s)] = max(v1, v2) 
                    
                
                if d_s == 2:
                    v3 = dp(idx + 1, 2) 
                    v4 = dp(idx + 1, 1) + prices[idx]

                    memo[(idx, d_s)] = max(v3, v4) 
                    
            return memo[(idx, d_s)]
            
            
        
        return dp(0, 1)