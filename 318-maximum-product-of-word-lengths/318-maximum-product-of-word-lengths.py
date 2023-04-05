class Solution:
    def maxProduct(self, words: List[str]) -> int:
      
        dic = []
        for i in range(len(words)):
            temp = 0
            for w in words[i]:
                ordo = ord(w) - 97
                shift = 1 << ordo
                temp |= shift
            dic.append((i, temp))
        maxim = 0    
        for i in range(len(dic)):
            for j in range(i + 1, len(dic)):
                ands = dic[i][1] & dic[j][1]
                if ands == 0:
                    maxim = max(maxim, len(words[dic[i][0]]) * len(words[dic[j][0]]))
                    
        return maxim            
                
                
                
        