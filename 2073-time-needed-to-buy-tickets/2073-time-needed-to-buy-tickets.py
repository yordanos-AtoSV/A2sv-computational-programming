class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        target = tickets[k]
        
        for i in range(len(tickets)):
            diff = tickets[i] - target
            if diff >= 0:
                ans += target
            else:
                ans += tickets[i]
            
            if i == k:
                target -= 1
        
        return ans
