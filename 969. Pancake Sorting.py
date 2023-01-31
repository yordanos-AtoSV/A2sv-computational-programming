class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:

        ans = []
        ptr = len(arr) - 1
  
        for i in range(len(arr)):
            maxi = arr[0] 
         
            for j in range(1, ptr + 1):
                maxi = max(maxi, arr[j]) 
            
            indice = arr.index(maxi)
       
            if indice != 0 :
               
                ans.append(indice + 1)
                
                arr[ : indice + 1] = arr[indice : : -1]
                ans.append(ptr + 1)
                
                arr[ : ptr+ 1] = arr[ptr : : -1]
                ptr -= 1
           
            else:
                ans.append(ptr + 1)
                arr[ : ptr+ 1] = arr[ptr : : -1]
                ptr -= 1
               

        return ans
