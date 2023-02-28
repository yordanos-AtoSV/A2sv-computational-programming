class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0:
            return 1
        if n < 0:
            return 1/self.power(x, abs(n))
        else:
            return self.power(x, n)
    def power(self , x:float, n: int) -> float:
        
        if n == 1:
            return x
        if n % 2 == 0: 
            left = self.power(x, n//2)
            return left * left
        else:
            right = self.power(x, n-1)
            return right * x

        