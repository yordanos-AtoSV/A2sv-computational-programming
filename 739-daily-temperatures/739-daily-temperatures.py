class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ans = [0] * len(temperatures)
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                temp = stack.pop()
                
                ans[temp] = i - temp 
                
            stack.append(i)
            
            
        return ans