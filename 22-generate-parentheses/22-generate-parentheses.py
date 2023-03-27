class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []
        
        def back(path, open, close):
            if len(path) == n * 2:
                ans.append("".join(path))
                return
            
            if open < n:
                path.append("(")
                
                back(path, open + 1, close)
                path.pop()
                
            if close < n and close < open:
                path.append(")")
               
                back(path, open, close + 1)
                path.pop()
                
       
        
        open = 0
        close = 0
        back([], open, close)
        return ans
                
        