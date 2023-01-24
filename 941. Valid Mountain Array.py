class Solution:
    def validMountainArray(self, array: List[int]) -> bool:
        flag = False
        if len(array) >= 3:   
            i = 0
            j = len(array)-1
            point1 = -5
            point2 = -5
            while(i < len(array)- 1 and j > 0):
                if array[i] < array[i+1]:
                    
                    i +=1
                    
                else:
                    point1 = i 
                    
                if array[j] < array[j - 1]:
                   
                    j -=1
                    
                else:
                    point2 = j
                    
                    
                if point1!= -5 and point2 != -5:
                    break
            if point1 == point2:
                flag = True 
            else:
               
                return flag
        else:
            
            return flag
        return flag
       
