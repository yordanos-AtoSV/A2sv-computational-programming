class Solution:
      def simplifyPath(self, path: str) -> str:
            path = path.split("/")
            stack = []
            for c in path:
                if c == "" or c == ".":
                    continue
                elif c =="..":
                    if stack:
                        stack.pop()
                else:
                    stack.append(c)
            
            return "/" + "/".join(stack)
                
                
                
