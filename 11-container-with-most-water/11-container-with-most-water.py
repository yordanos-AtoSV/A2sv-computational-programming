class Solution:
    def maxArea(self, height: List[int]) -> int:
        p1 = 0 
        p2 = len(height) - 1 
        d = 0
        maxi = 0
        minin = 0
        while p1 < p2:
            d = p2 - p1
            mini = min (height[p2], height[p1])
            maxi = max (maxi, d*mini)
            if mini == height[p2]:
                p2 -= 1 
            else:
                p1 += 1
        return maxi
 
        
        