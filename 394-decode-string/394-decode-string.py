class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ""
        
        for i in range(len(s)):
            
            if stack and stack[-1].isdigit() and s[i].isdigit():
                stack[-1] += s[i]
                
                continue
            
            if stack and stack[-1].isalpha() and s[i].isalpha():
                stack[-1] += s[i]
            
                continue
         
                
            if s[i] == "]":
                
                temp2 = ""
                while stack and stack[-1] != "[":
                    temp = stack.pop()
                    
                if stack:    
                    stack.pop()
            
                    num = int(stack.pop())
                
                for i in range(num):
                    temp2 += temp
                    
        
                if stack and stack[-1].isalpha():    
                    stack[-1] +=temp2
                if stack and not stack[-1].isalpha():
                    stack.append(temp2)
                if not stack:
                    ans += temp2
          
                
                continue
            
            stack.append(s[i])
            
           
        if stack:
            ans += stack[-1]
            
        return ans