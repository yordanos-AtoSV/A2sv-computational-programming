class Solution:
    def maxLength(self, arr: List[str]) -> int:
        
        temp = set()
        def unique (temp, s):
            counter = Counter(temp) + Counter(s)
            return max(counter.values()) > 1
        
        def backtrack(idx):
            if idx == len(arr):
                return len(temp)
            
            res = 0
            
            if not unique(temp, arr[idx]):
                for c in arr[idx]:
                    temp.add(c)
                res = backtrack(idx + 1)
                
                for c in arr[idx]:
                    temp.remove(c)
                    
            return max(res, backtrack(idx + 1))
                
        
        return backtrack(0)