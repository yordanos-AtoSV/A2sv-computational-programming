#User function Template for python3

class Solution:
    
    def heapify(self,arr, n, i):
            left = (2 * i) + 1
            right = (2 * i) + 2 

            while (n > left and arr[i] < arr[left]) or (n > right and arr[i] < arr[right]):
                if n > left and n > right:
                    if arr[left] > arr[right]:
                        max_child = left
                    else:
                        max_child = right

                elif n > left:
                    max_child = left
                else:
                    max_child = right

                arr[i], arr[max_child] = arr[max_child], arr[i]
                i = max_child
                left = (2 * i) + 1
                right = (2 * i) + 2
                
                
 
    def buildHeap(self,arr,n):
            
            for i in range(n // 2 - 1, -1, -1):
                self.heapify(arr, n, i)
         
            
    

    def HeapSort(self, arr, n):
        self.buildHeap(arr, n )  
        for i in range(n - 1, -1, -1):
            arr[i], arr[0] = arr[0], arr[i]
            self.heapify(arr, i, 0)
            
