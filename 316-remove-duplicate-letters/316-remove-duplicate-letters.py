class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        stack = []
        freq = Counter(s)
        seen = defaultdict(str)
        
        for c in freq:
            seen[c] = "F"
            
        stack.append(s[0])
        seen[s[0]] = "T"
        freq[s[0]] -= 1
        
        for c in s[1:]:
            if seen[c] == "F":
                if stack[-1] < c:
                    stack.append(c)
                    freq[c] -= 1
                else:
                    while stack and c <= stack[-1]:
                        if freq[stack[-1]] != 0:
                            seen[stack[-1]] = "F"
                            stack.pop()
                        else:
                            break
                    stack.append(c)
                    freq[c] -= 1
                            
                seen[c] = "T"
              
            else:
                freq[c] -= 1
                continue
                
        return "".join(stack)
                            
            
                    
                    
        return "m"

                    
            