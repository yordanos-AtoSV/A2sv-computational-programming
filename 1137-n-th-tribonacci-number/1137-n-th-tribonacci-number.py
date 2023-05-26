class Solution:
    def tribonacci(self, n: int) -> int:
        if n < 2:
            return n
        arr = [0,0, 1, 1]
        for i in range(3, n + 1):
            arr[0] = arr[1] 
            arr[1] = arr[2]
            arr[2] = arr[3]
            arr[3] = arr[2] + arr[1] + arr[0]
            
        return arr[3]
            
            