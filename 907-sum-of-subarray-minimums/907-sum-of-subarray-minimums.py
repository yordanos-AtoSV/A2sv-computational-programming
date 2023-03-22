class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int: 
        
        mod = pow(10,9) + 7
        ans = 0
        stack = [-1]
        
        
        for i in range( len(arr) + 1 ):
            if stack[-1] != -1:
                while stack[-1] != -1 and (i == len(arr) or arr[i] < arr[stack[-1]]):
                    mid = stack[-1]
                    l = stack[-2]
                    r = i 
                    temp = (mid - l) * (r - mid) 
                    ans += temp * arr[stack[-1]]
                
                    stack.pop()
                
            stack.append(i)
            
            
        return ans % mod
            
            
            
            