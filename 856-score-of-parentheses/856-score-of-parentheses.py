class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        ans = 0
        val = 0
        for c in s:
            if c == "(":
                stack.append(0)
            else:
                mul = stack.pop()
                if mul == 0:
                    val = 1
                else:
                    val = mul * 2
                    
                if not stack:
                    ans += val
                else:
                    stack[-1] += val
                    
        return ans