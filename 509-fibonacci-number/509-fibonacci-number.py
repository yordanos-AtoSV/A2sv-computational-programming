class Solution:
    def fib(self, n: int) -> int:
        if n < 2:
            return n
        else:
            arr = [0,0,1]
            for i in range(2, n + 1):
                arr[0] = arr[1]
                arr[1] = arr[2]
                arr[2] = arr[1] + arr[0]
                
            return arr[2]

        