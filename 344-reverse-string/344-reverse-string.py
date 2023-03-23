class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        def reverse(p1, p2):
            if p1 >= p2:
                return
            s[p1], s[p2] = s[p2], s[p1]
            
            reverse(p1 + 1, p2 - 1)
            
        reverse(0, len(s) - 1)
        
        return s
        
