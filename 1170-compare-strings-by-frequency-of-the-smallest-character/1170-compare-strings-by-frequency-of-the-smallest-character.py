class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        countp = []
        ans = []

        for w in words:
            counter = Counter(w)
            x = min(w)
            countp.append(counter[x])
            
        countp.sort()
        
        for w in queries:
            counter = Counter(w)
            x = min(w)
            y = counter[x]
      
            l = 0
            r = len(countp) - 1
            leftmost = None
            while l <= r :
                mid = (l + r) // 2
                temp = countp[mid]
                if temp > y :
                    leftmost = mid
                    r = mid - 1
                else:
                    l = mid + 1
                 
            if leftmost == None:
                ans.append(0)
            else:
                ans.append(len(countp) - leftmost)
                
        return ans
            
                        
                        
                        
                            
                            
                    
                


        
