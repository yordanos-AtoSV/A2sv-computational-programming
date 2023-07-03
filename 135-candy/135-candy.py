class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
   [1,2,87,87,87,2,1]
   
   [1,2,1,1,1,1,1]


        """
        n = len(ratings)
        res = [1] * n
        
        for i in range(n - 1):
            if ratings[i] < ratings[i + 1]:
                if res[i] >= res[i + 1]:
                    temp = res[i] - res[i + 1]
                    res[i + 1] += temp + 1
                
                
        for i in range(n - 1, 0, -1 ):
            if ratings[i] < ratings[i - 1]:
            
                if res[i] >= res[i - 1]:
                    
                    temp = res[i] - res[i - 1]
                    res[i - 1] += temp + 1
                  

   
        
        return sum(res)