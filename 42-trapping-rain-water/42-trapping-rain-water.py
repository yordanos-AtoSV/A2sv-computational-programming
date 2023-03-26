class Solution:
    def trap(self, height: List[int]) -> int:
        ans = 0
        stack = []
        
        for i in range(len(height)):
            while stack and height[stack[-1]] < height[i]:
                temp = stack.pop()
                if stack:
                    temp2 = height[stack[-1]] - height[temp]
                    if  height[stack[-1]] > height[i]:
                        temp2 = height[i] - height[temp]
                    width = (i - stack[-1]) - 1
          
                    ans += width * temp2
  
                
            stack.append(i)
            
        return ans
        