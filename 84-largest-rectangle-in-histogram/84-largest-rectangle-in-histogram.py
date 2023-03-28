class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        ans = 0
        for i in range(len(heights)):
            while stack and heights[stack[-1]] > heights[i]:
                temp = stack.pop()
                if stack:
                    length = (i - stack[-1]) - 1
                else:
                    length = i
                    
                ans = max(ans, length * heights[temp])
                
                
                
            stack.append(i)
            
            
        
        while stack:
            tempo = stack.pop()
            if stack:
                length = (len(heights) - stack[-1]) - 1

            else:
                length = len(heights)

            ans = max(ans, length * heights[tempo])
            
                      
                
        return ans
                
        
        